#!/usr/bin/env python

import sys, os, sh, platform

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'Ogitor'
    dirname = 'ogitor'

    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'https://bitbucket.org/jacmoe/ogitor' ] )
        # FIXME: apply patch

    def compile( self, source_dir, build_dir, install_dir ):
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        runpath_dir = os.path.join( package_source_dir, 'RunPath' )
        if ( not os.path.exists( os.path.join( runpath_dir, 'media.zip' ) ) ):
            sh.cd( runpath_dir )
            sh.wget( '--no-check-certificate', 'https://bitbucket.org/jacmoe/ogitor/downloads/media.zip' )
            sh.unzip( 'media.zip' )
        if ( not os.path.exists( os.path.join( runpath_dir, 'projects.zip' ) ) ):
            sh.cd( runpath_dir )
            sh.wget( '--no-check-certificate', 'https://bitbucket.org/jacmoe/ogitor/downloads/projects.zip' )
            sh.unzip( 'projects.zip' )
        sh.mkdir( '-p', package_build_dir )
        sh.cd( package_build_dir )
        if ( platform.system() == 'Darwin' ):
            sh.cmake(
                '-G', 'Xcode',
                '-D', 'CMAKE_INSTALL_PREFIX=%s' % install_dir,
                '-D', 'CMAKE_MODULE_PATH=%s' % os.path.join( install_dir, 'CMake' ),
                package_source_dir,
                _out = sys.stdout )
            sh.xcodebuild( '-configuration', 'Release', _out = sys.stdout )
        else:
            sh.cmake(
                '-D', 'CMAKE_INSTALL_PREFIX=%s' % install_dir,
                '-D', 'CMAKE_MODULE_PATH=%s' % os.path.join( install_dir, 'lib/OGRE/cmake' ),
                package_source_dir,
                _out = sys.stdout )
            sh.make( '-j4', 'VERBOSE=1', _out = sys.stdout )
            sh.make.install( _out = sys.stdout )
