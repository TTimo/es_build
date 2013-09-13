#!/usr/bin/env python

import sys, os

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'Ogre'
    dirname = 'ogre'
    
    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'https://bitbucket.org/sinbad/ogre/', '-r', 'v1-8' ] )

    def compile( self, source_dir, build_dir, install_dir ):
        import sh
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        sh.mkdir( '-p', package_build_dir )
        sh.cd( package_build_dir )
        sh.cmake( '-D', 'CMAKE_INSTALL_PREFIX=%s' % install_dir, package_source_dir, _out = sys.stdout )
        sh.make( '-j4', 'VERBOSE=1', _out = sys.stdout )
        sh.make.install( _out = sys.stdout )

