#!/usr/bin/env python

import os, pprint

# defaults
PACKAGES_DIR='packages'

_TOP_DIR = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
SOURCE_DIR = os.path.join( _TOP_DIR, 'source' )
BUILD_DIR = os.path.join( _TOP_DIR, 'build' )
INSTALL_DIR = os.path.join( _TOP_DIR, 'run' )

# the build system supports multiple flavors for some customized things
# for instance the AWS Ubuntu 10.x we use for Linux binaries is "ubuntu_10"
FLAVOR = "default"

# put customized site configuration in a config file that does not get checked in
ES_CONFIG_SITE_FILENAME='es_config_site.py'
if ( os.path.exists( ES_CONFIG_SITE_FILENAME ) ):
#    print( 'Found site configuration:' )
    es_config_site = __import__( ES_CONFIG_SITE_FILENAME[:-3], globals(), locals() )
    # merge into globals() .. there is probably a better way to do this?
    for ( k, v ) in es_config_site.__dict__.items():
        if ( not k[0].isupper() ):
            continue
#        print( '  %s=%s' % ( str( k ), str( v ) ) )
        globals()[k] = v

if ( __name__ == '__main__' ):
    # if executed directly, print the configuration as we see it
    for ( name, value ) in sorted( globals().items() ):
        if ( not name[0].isupper() ):
            continue
        print( '%s=%s' % ( name, repr( value ) ) )


