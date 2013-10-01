# Chocolatey is awesome package management on Windows
iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
# RS checks that the script ran with no errors, but chocolatey leaves something in $error even though it ran fine?
$error.clear()

# We only need git and python
C:\Chocolatey\bin\chocolatey.bat install git.install
C:\Chocolatey\bin\chocolatey.bat install python

# Update global PATH setting as needed
$set_globally = 0

if ( !( $Env:Path | Select-String -SimpleMatch "C:\Chocolatey\bin" ) ) {
  $Env:Path="$Env:Path;C:\Chocolatey\bin"
  $set_globally = 1
}

if ( !( $Env:Path | Select-String -SimpleMatch "C:\Python27" ) ) {
  $Env:Path="$Env:Path;C:\Python27"
  $set_globally = 1
}

if ( !( $Env:Path | Select-String -SimpleMatch "C:\Program Files (x86)\Git\bin" ) ) {
  $Env:Path="$Env:Path;C:\Program Files (x86)\Git\bin"
  $set_globally = 1
}

if ( $set_globally -ne 0 ) {
  Write-Host "Set the PATH to $Env:Path"
  Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value "$Env:Path"
}

# Checkout the rest of es_build
if ( !( Test-Path D:\es_core\es_build ) ) {
  cd D:\
  MkDir D:\es_core
  cd D:\es_core
  git clone https://github.com/TTimo/es_build.git
} else {
  cd D:\es_core\es_build
  git pull
}

# Continue execution with the build system prerequisites
python D:\es_core\es_build\prerequisites\windows\execute.py
