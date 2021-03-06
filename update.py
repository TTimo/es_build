#!/usr/bin/env python

import pprint

import es_config
import helpers

if ( __name__ == '__main__' ):
    for package_module in helpers.iterate_packages( es_config.PACKAGES_DIR ):
        package = package_module.PackageDetails()
        print( 'Updating source for %s:' % package.name )
        package.source( es_config.SOURCE_DIR )
