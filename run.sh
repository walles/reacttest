#!/bin/bash

set -e

(
  cd webui
  npm run build
)

# FIXME: Start the Python server here, serving from webui/build
