#!/bin/bash

set -e

(
  cd webui
  npm run build
)

./webserver.py
