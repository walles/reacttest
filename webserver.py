#!/usr/bin/env python

import BaseHTTPServer
import webbrowser

# "0" gets us a random port: https://stackoverflow.com/a/442074/473672
server_address = ('localhost', 0)

# FIXME: This thing should serve files from webui/build
httpd = BaseHTTPServer.HTTPServer(server_address, BaseHTTPServer.BaseHTTPRequestHandler)
url = "http://localhost:" + str(httpd.server_port)
print("Serving on " + url)

# FIXME: There's a race condition here; we should really start serving before we
# open the browser. How do we even know when the web server has started serving?
webbrowser.open(url)
httpd.serve_forever()
