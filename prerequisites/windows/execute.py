# this is either executed manually, or by the powershell bootstrap

import subprocess

if ( __name__ == '__main__' ):
    # continue installation of system packages with Chocolatey
    for package in [
	'VisualStudio2012WDX',
	'directx',
	'hg',
	'svn',
	'AWSTools.Powershell',
	'Wget',
	'emacs',
	'GoogleChrome' ]:
        subprocess.check_call( [ r'C:\Chocolatey\bin\chocolatey.bat', 'install', package ] )

    # TODO: install a recent enough cmake

    # TODO: install pip and setuptools
    # see http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

    # TODO: leverage pip to install the latest sh and s3cmd

