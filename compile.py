#!/usr/bin/env python

import argparse

import es_config
import helpers

if ( __name__ == '__main__' ):
    parser = argparse.ArgumentParser()
    parser.add_argument( '--target' )
    args = parser.parse_args()
    for package_module in helpers.iterate_packages( es_config.PACKAGES_DIR ):
        package = package_module.PackageDetails()
        if ( args.target is not None and package.name.lower() != args.target.lower() ):
            print( 'Skip %s' % package.name )
            continue
        print( 'Compile %s:' % package.name )
        package.compile( es_config.SOURCE_DIR, es_config.BUILD_DIR, es_config.INSTALL_DIR )
