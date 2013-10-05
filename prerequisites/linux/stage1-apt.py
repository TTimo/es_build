#!/usr/bin/env python

import sys, os, subprocess

try:
    import es_config
except:
    import imp
    es_config = imp.load_source(
        'es_config',
        os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..', '..', 'es_config.py' ) ) )

packages = [
    'gettext',
    'libcurl4-gnutls-dev',
    'libexpat1-dev',
    'libfreeimage-dev',
    'libfreetype6-dev',
    'libgl1-mesa-dev',
    'libglu1-mesa-dev',
    'libgtk2.0-dev',
    'libqt4-dev',
    'libssl-dev',
    'libwxgtk2.8-dev',
    'libx11-dev',
    'libxaw7-dev',
    'libxt-dev',
    'libz-dev',
    'libzzip-dev',
    'mercurial',
    'mesa-common-dev',
    'mesa-utils',
    'pkg-config',
    'python-pip',
    'wx-common',
    ]

if ( es_config.FLAVOR == 'ubuntu_10' ):
    packages.append( 'libboost1.40-all-dev' )
else:
    packages.append( 'libboost-all-dev' )
    packages.append( 'cmake' )

if ( __name__ == '__main__' ):
    subprocess.check_call( 'apt-get update', shell = True )
    for package in packages:
        install_cmd = 'apt-get install -q -y %s' % package
        print( install_cmd )
        subprocess.check_call( install_cmd, shell = True )
