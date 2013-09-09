#!/bin/bash -e
# use this script to bootstrap a RightScale Linux instance with es_build
# package dependencies: git python

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

cd "$ES_BUILD_TOPDIR"
if [ -d "$ES_BUILD_DIRNAME" ]
then
  cd "$ES_BUILD_DIRNAME"
  git pull
else
  git clone "$ES_BUILD_GITURL" "$ES_BUILD_DIRNAME"
fi
