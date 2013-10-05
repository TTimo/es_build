#!/usr/bin/env python

import os, pprint, imp

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
es_site_config_path = os.path.abspath( os.path.join( os.path.dirname( __file__ ), 'es_site_config.py' ) )
if ( os.path.exists( es_site_config_path ) ):
#    print( 'Loading site configuration %s' % repr( es_site_config_path ) )
    es_site_config = imp.load_source(
        'es_site_config',
        es_site_config_path )
    # merge into globals() ..
    for ( k, v ) in es_site_config.__dict__.items():
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


