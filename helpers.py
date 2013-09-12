#!/usr/bin/env python

import os, pprint, traceback

def iterate_packages( directory ):
    for package_name in os.listdir( directory ):
        if ( not package_name.endswith( '.py' ) ):
            continue
        if ( package_name in [ '__init__.py', 'package_helpers.py' ] ):
            continue
        module_name = package_name[:-3]
        module_path = '%s.%s' % ( directory, module_name )
        try:
            package_module = __import__( module_path, globals(), locals(), [ 'PackageDetails' ] )
        except:
            traceback.print_exc()
            print( 'Skip %s: Import failed' % module_path )
            continue
        if ( not hasattr( package_module, 'PackageDetails' ) ):
            print( 'Skip %s: Does not define PackageDetails' % module_path )
            continue
        yield package_module
