#!/usr/bin/env python

import sys, os

import package_helpers

class PackageDetails( package_helpers.PackageTemplate ):
    name = 'es_core'
    dirname = 'es_core'

    def source( self, source_dir ):
        package_helpers.git_clone( source_dir, self.dirname, [ 'https://github.com/TTimo/es_core.git' ] )
