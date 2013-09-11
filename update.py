#!/usr/bin/env python

import os, pprint, traceback

PACKAGES_DIR='packages'
SOURCE_DIR='/opt/source/'

if ( __name__ == '__main__' ):

    for package_name in os.listdir( PACKAGES_DIR ):
        if ( not package_name.endswith( '.py' ) ):
            continue
        if ( package_name == '__init__.py' ):
            continue
        module_name = package_name[:-3]
        module_path = '%s.%s' % ( PACKAGES_DIR, module_name )
        try:
            package_module = __import__( module_path, globals(), locals(), [ 'PackageDetails' ] )
            assert( hasattr( package_module, 'PackageDetails' ) )
        except:
            traceback.print_exc()
            print( 'Problem importing %s' % module_path )
            continue
        if ( not hasattr( package_module, 'PackageDetails' ) ):
            print( 'Module %s does not define PackageDetails' % module_path )
            continue
        
        print( 'Updating %s' % module_path )
        package_module.PackageDetails().source( SOURCE_DIR )
