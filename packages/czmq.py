#!/usr/bin/env python

import sys, os

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'czmq'
    dirname = 'czmq'

    def source( self, source_dir ):
        package_helpers.git_clone( source_dir, self.dirname, [ 'git://github.com/zeromq/czmq.git' ] )
