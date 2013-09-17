#!/usr/bin/env python

import sys, os

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'SDL'
    dirname = 'SDL'
    
    def source( self, source_dir ):
        package_helpers.mercurial_clone( source_dir, self.dirname, [ 'http://hg.libsdl.org/SDL' ] )
