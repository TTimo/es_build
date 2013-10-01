#!/usr/bin/env python

import sys, os, platform, sh

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'SDL'
    dirname = 'SDL'
    
    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'http://hg.libsdl.org/SDL' ] )
        # FIXME: apply patch

    def compile( self, source_dir, build_dir, install_dir ):
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        sh.mkdir( '-p', package_build_dir )
        sh.cd( package_build_dir )
        if ( platform.system() == 'Darwin' ):
            sh.cmake( '-G', 'Xcode', '-D', 'CMAKE_INSTALL_PREFIX=%s' % install_dir, package_source_dir, _out = sys.stdout )
            sh.xcodebuild( '-scheme', 'install', '-configuration', 'Release', _out = sys.stdout )
        else:
            sh.cmake( 'CMAKE_INSTALL_PREFIX=%s' % install_dir, package_source_dir, _out = sys.stdout )
            sh.make( '-j4', 'VERBOSE=1', _out = sys.stdout )
            sh.make.install( _out = sys.stdout )

        
