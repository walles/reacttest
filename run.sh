#!/bin/bash

set -e

if [ "$VIRTUAL_ENV" ] ; then
  echo 'ERROR: Already in a virtualenv, do "deactivate" first and try again'
  exit 1
fi

if [ ! -d env ] ; then
  virtualenv env
fi
. ./env/bin/activate
pip install -r requirements.txt

time (
  cd webui
  npm run build
)

./webserver.py
