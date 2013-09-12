#!/usr/bin/env python

import es_config
import helpers

if ( __name__ == '__main__' ):
    for package_module in helpers.iterate_packages( es_config.PACKAGES_DIR ):
        package = package_module.PackageDetails()
        print( 'Compile %s:' % package.name )
        package.compile( es_config.SOURCE_DIR, es_config.BUILD_DIR, es_config.INSTALL_DIR )
