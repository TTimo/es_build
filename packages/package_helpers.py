#!/usr/bin/env python

import os, subprocess

def mercurial_clone( top_dir, clone_dir, clone_args ):
    os.chdir( top_dir )
    if ( os.path.exists( clone_dir ) ):
        os.chdir( clone_dir )
        subprocess.check_call( [ 'hg', 'update' ] )
    else:
        subprocess.check_call( [ 'hg', 'clone', ] + clone_args )
        assert( os.path.exists( clone_dir ) )

class PackageTemplate( object ):
    name = 'Package Template'

    def source( self, source_dir ):
        pass

    def compile( self, source_dir, build_dir, install_dir ):
        pass
