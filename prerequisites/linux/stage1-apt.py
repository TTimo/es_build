#!/usr/bin/env python

import subprocess

packages = [
    'python-pip',
    'mercurial',
    'libx11-dev',
    'libxt-dev',
    'libfreetype6-dev',
    'mesa-common-dev',
    'pkg-config',
    'libcurl4-gnutls-dev',
    'libexpat1-dev',
    'gettext',
    'libz-dev',
    'libssl-dev',
    ]

if ( __name__ == '__main__' ):
    subprocess.check_call( 'apt-get update', shell = True )
    install_cmd = 'apt-get install -q -y %s' % ' '.join( packages )
    print( install_cmd )
    subprocess.check_call( install_cmd, shell = True )
