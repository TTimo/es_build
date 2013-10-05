#!/usr/bin/env python

import os, subprocess, sh

try:
    import es_config
except:
    import imp
    es_config = imp.load_source(
        'es_config',
        os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..', '..', 'es_config.py' ) ) )

# FIXME: should be setup by the bootstrap etc.
BUILD_DIR="/opt/es_build/prerequisites/linux/build"
PREFIX="/usr/local"

def install_cmake( build_dir, prefix ):
    cmake_archive='cmake-2.8.11.2'
    sh.cd( build_dir )
    sh.wget( '-nc', 'http://www.cmake.org/files/v2.8/%s.tar.gz' % cmake_archive )
    sh.tar( 'xvzf', '%s.tar.gz' % cmake_archive )
    sh.cd( cmake_archive )
    subprocess.check_call( [ './configure', '--prefix', PREFIX ], shell = True )
    sh.make( '-j4' )
    sh.make.install()

def upgrade_git( build_dir, prefix ):
    sh.cd( build_dir )
    if ( os.path.exists( 'git' ) ):
        sh.cd( 'git' )
        sh.git.pull()
    else:
        sh.git.clone( 'https://github.com/git/git' )
        sh.cd( 'git' )
    sh.make( 'prefix=%s' % prefix, '-j4' )
    sh.make.install( 'prefix=%s' % prefix )

if ( __name__ == '__main__' ):
    if ( es_config.FLAVOR == 'default' ):
        continue
    # TODO: compile latest gcc
    upgrade_git( BUILD_DIR, PREFIX )
    install_cmake( BUILD_DIR, PREFIX )
