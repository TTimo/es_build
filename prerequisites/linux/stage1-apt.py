#!/usr/bin/env python

import subprocess

packages = [
    'gettext',
    'libboost1.40-all-dev',
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

if ( __name__ == '__main__' ):
    subprocess.check_call( 'apt-get update', shell = True )
    install_cmd = 'apt-get install -q -y %s' % ' '.join( packages )
    print( install_cmd )
    subprocess.check_call( install_cmd, shell = True )
