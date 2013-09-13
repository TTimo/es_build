#!/usr/bin/env python

import sys, os, sh

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'Ogre Meshy'
    dirname = 'ogremeshy'

    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'https://bitbucket.org/dark_sylinc/ogremeshy/' ] )
        # FIXME: patch up CMakeLists.old.1.8.txt before copying it over (comment out the CMAKE_MODULE_PATH part)
#        sh.cp( '-v', os.path.join( source_dir, self.dirname, 'CMakeLists.old.1.8.txt' ), os.path.join( source_dir, self.dirname, 'CMakeListst.txt' ), _out = sys.stdout )

    def compile( self, source_dir, build_dir, install_dir ):
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        sh.mkdir( '-p', package_build_dir )
        sh.cd( package_build_dir )
        sh.cmake(
            '-D', 'CMAKE_INSTALL_PREFIX=%s' % install_dir,
            '-D', 'CMAKE_MODULE_PATH=%s' % os.path.join( install_dir, 'lib/OGRE/cmake' ),
            package_source_dir,
            _out = sys.stdout )
        sh.make( '-j4', 'VERBOSE=1', _out = sys.stdout )
        sh.make.install( _out = sys.stdout )
        # FIXME: copy wrapper and helper scripts, external libraries that need to be packaged etc.
