#!/usr/bin/env python

import argparse, pprint

import es_config
import helpers

if ( __name__ == '__main__' ):
    parser = argparse.ArgumentParser()
    parser.add_argument( '--only', required = False )
    # skip isn't terribly useful
    # maybe a 'prompt' option?
    parser.add_argument( '--skip', action = 'append', required = False )
    args = parser.parse_args()
    args_skip = []
    if ( args.skip is not None ):
        args_skip = [ a.lower() for a in args.skip ]
    for package_module in helpers.iterate_packages( es_config.PACKAGES_DIR ):
        package = package_module.PackageDetails()
        if ( ( args.only is not None and package.name.lower() != args.only.lower() )
             or package.name.lower() in args_skip ):
            print( 'Skip %s' % package.name )
            continue
        print( 'Compile %s:' % package.name )
        package.compile( es_config.SOURCE_DIR, es_config.BUILD_DIR, es_config.INSTALL_DIR )
