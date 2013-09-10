#!/usr/bin/env python

import subprocess

packages = [
    'pip',
    'sh',
]

pre_packages = [
    's3cmd',
]

if ( __name__ == '__main__' ):
    for pname in packages:
        cmd = 'pip install -U %s' % pname
        print( cmd )
        subprocess.check_call( cmd, shell = True )

    for pname in pre_packages:
        cmd = 'pip install -U --pre %s' % pname
        print( cmd )
        subprocess.check_call( cmd, shell = True )
    
    subprocess.check_call( 'pip --version', shell = True )
