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

        # Invoke autogen.sh if configure script doesn't exist
        if not os.path.exists( '%s%s%s' % ( package_source_dir, os.sep, 'configure' ) ):
            sh.cd( package_source_dir )
            subprocess.check_call( [ os.path.join( package_source_dir, 'autogen.sh' ) ], shell = True ),

        # NOTE: there are problems with cmake support on this still
        sh.cd( package_build_dir )
        subprocess.check_call( [ os.path.join( package_source_dir, 'configure' ), '--prefix=%s' % install_dir ], shell = True )
        sh.make( '-j4', _out = sys.stdout )
        sh.make.install( _out = sys.stdout )
