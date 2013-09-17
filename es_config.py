#!/usr/bin/env python

import os, pprint

_TOP_DIR = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
SOURCE_DIR = os.path.join( _TOP_DIR, 'source' )
BUILD_DIR = os.path.join( _TOP_DIR, 'build' )
INSTALL_DIR = os.path.join( _TOP_DIR, 'run' )

PACKAGES_DIR='packages'

if ( __name__ == '__main__' ):
    # if executed directly, print the configuration as we see it
    for ( name, value ) in sorted( globals().items() ):
        if ( not name[0].isupper() ):
            continue
        print( '%s=%s' % ( name, repr( value ) ) )


