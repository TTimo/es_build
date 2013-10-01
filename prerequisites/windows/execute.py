# this is either executed manually, or by the powershell bootstrap

import sys, os, subprocess

if ( __name__ == '__main__' ):
    # setup current directory
    os.chdir( os.path.abspath( os.path.dirname( __file__ ) ) )
    print( 'Entering %s in %s' % ( __file__, os.getcwd() ) )

    # continue installation of system packages with Chocolatey
    for package in [
	'VisualStudio2012WDX',
	'directx',
	'hg',
	'svn',
	'AWSTools.Powershell',
	'Wget',
	'emacs',
	'GoogleChrome',
    ]:
        subprocess.check_call( [ r'C:\Chocolatey\bin\chocolatey.bat', 'install', package ] )

    # install pip
    if ( os.path.exists( 'ez_setup.py' ) ):
        os.unlink( 'ez_setup.py' )
    subprocess.check_call( [ r'C:\Chocolatey\bin\wget.bat', '--no-check-certificate', 'https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py' ] )
    subprocess.check_call( [ 'python', 'ez_setup.py' ] )

    if ( os.path.exists( 'get-pip.py' ) ):
        os.unlink( 'get-pip.py' )
    subprocess.check_call( [ r'C:\Chocolatey\bin\wget.bat', '--no-check-certificate', 'https://raw.github.com/pypa/pip/master/contrib/get-pip.py' ] )
    subprocess.check_call( [ 'python', 'get-pip.py' ] )

    # TODO: add C:\Python27\Script to the system wide path if needed

    # now that we have pip, use it
    subprocess.check_call( [ r'C:\Python27\Scripts\pip.exe', 'install', '-U', '--pre', 's3cmd' ] )
    # ouch, sh is not supported on Windows ..
    # https://github.com/amoffat/sh/issues/155
#    subprocess.check_call( [ r'C:\Python27\Scripts\pip.exe', 'install', '-U', 'sh' ] )

    # install a recent enough cmake
    subprocess.check_call( [ r'C:\Chocolatey\bin\wget.bat', 'http://www.cmake.org/files/v2.8/cmake-2.8.11.2-win32-x86.zip' ] )
    # TODO: expand it to a top path, setup system wide path if needed

