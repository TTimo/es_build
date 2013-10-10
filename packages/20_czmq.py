#!/usr/bin/env python

import sys, os, subprocess, platform, sh

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'czmq'
    dirname = 'czmq'

    def source( self, source_dir ):
        package_helpers.git_clone( source_dir, self.dirname, [ 'git://github.com/zeromq/czmq2-x.git', 'czmq' ] )

    def compile( self, source_dir, build_dir, install_dir ):
        package_source_dir = os.path.join( source_dir, self.dirname )
        assert( os.path.exists( package_source_dir ) )
        package_build_dir = os.path.join( build_dir, self.dirname )
        sh.mkdir( '-p', package_build_dir )

        sh.cd( package_source_dir )
        subprocess.check_call( [ os.path.join( package_source_dir, 'autogen.sh') ] )

        sh.cd( package_build_dir )
        subprocess.check_call( [ os.path.join( package_source_dir, 'configure' ), '--prefix=%s' % install_dir, '--with-libzmq=%s' % install_dir ] )
        sh.make( '-j4', _out = sys.stdout )
        sh.make.install( _out = sys.stdout )
