#!/usr/bin/env python

import os, subprocess

class PackageDetails( object ):
    dirname = 'ogre'

    def source( self, source_dir ):
        os.chdir( source_dir )
        if ( os.path.exists( self.dirname ) ):
            os.chdir( self.dirname )
            subprocess.check_call( [ 'hg', 'update' ] )
        else:
            subprocess.check_call( [ 'hg', 'clone', 'https://bitbucket.org/sinbad/ogre/', '-r', 'v1-8' ] )
            assert( os.path.exists( self.dirname ) )
