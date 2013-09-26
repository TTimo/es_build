#!/usr/bin/env python

import sys, os, platform, sh, subprocess

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'libzmq'
    dirname = 'libzmq'

    def source( self, source_dir ):
        package_helpers.git_clone( source_dir, self.dirname, [ 'https://github.com/zeromq/zeromq3-x.git', 'libzmq' ] )

    def compile( self, source_dir, build_dir, install_dir ):
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        sh.mkdir( '-p', package_build_dir )
        sh.cd( package_build_dir )
        # NOTE: there are problems with cmake support on this still
        subprocess.check_call( [ os.path.join( package_source_dir, 'configure' ), '--prefix=%s' % install_dir ], shell = True )
        sh.make( '-j4', _out = sys.stdout )
        sh.make.install( _out = sys.stdout )
