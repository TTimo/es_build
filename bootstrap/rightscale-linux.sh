#!/bin/bash -e
# use this script to bootstrap a RightScale Linux instance with es_build
# package dependencies: git-core python

if [ "x$ES_BUILD_TOPDIR" == "x" ]
then
  ES_BUILD_TOPDIR="/opt"
fi

if [ "x$ES_BUILD_DIRNAME" == "x" ]
then
  ES_BUILD_DIRNAME="es_build"
fi

if [ "x$ES_BUILD_GITURL" == "x" ]
then
  ES_BUILD_GITURL="https://github.com/TTimo/es_build.git"
fi

if [ "x$AWS_ACCESS_KEY_ID" == "x" ]
then
  AWS_ACCESS_KEY_ID="MISSING"
fi

if [ "x$AWS_SECRET_ACCESS_KEY" == "x" ]
then
  AWS_SECRET_ACCESS_KEY="MISSING"
fi

cat >$HOME/.s3cfg <<EOL
[default]
access_key = $AWS_ACCESS_KEY_ID
secret_key = $AWS_SECRET_ACCESS_KEY
EOL

# system git is needed for the initial checkout
# but after that a newer git needs to be used - otherwise hangs
if [ -e "/usr/local/bin/git" ]
then
  GIT=/usr/local/bin/git
else
  GIT=git
fi

cd "$ES_BUILD_TOPDIR"
if [ -d "$ES_BUILD_DIRNAME" ]
then
  cd "$ES_BUILD_DIRNAME"
  $GIT pull
else
  $GIT clone "$ES_BUILD_GITURL" "$ES_BUILD_DIRNAME"
fi

