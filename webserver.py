#!/usr/bin/env python

import BaseHTTPServer

# "0" gets us a random port: https://stackoverflow.com/a/442074/473672
server_address = ('localhost', 0)

# FIXME: This thing should serve files from webui/build
httpd = BaseHTTPServer.HTTPServer(server_address, BaseHTTPServer.BaseHTTPRequestHandler)
print("Serving on http://localhost:" + str(httpd.server_port))

httpd.serve_forever()
