#!/usr/bin/env python

import BaseHTTPServer
import webbrowser
import psutil
import shutil
import json
import os


# Serve files from webui/build
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_get_processes(self):
        processes = []
        for process in psutil.process_iter():
            processes.append({
                "pid": process.pid,
                "ppid": process.ppid(),
                "name": process.name(),
            })

        json_string = json.dumps({
            "processes": processes
        })

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_string)

    def do_GET(self):
        if self.path == "/processes":
            self.do_get_processes()
            return

        path = self.path.lstrip('/')
        path = path.split('#', 1)[0]
        path = path.split('?', 1)[0]

        if ".." in path:
            self.send_error(404, "No .. allowed in URL")
            return
        if "//" in path:
            self.send_error(404, "No // allowed in URL")
            return

        if path.endswith('/') or not path:
            path += "index.html"
        my_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(my_path, "webui", "build", path)
        # print("Serving request <" + self.path + "> from <" + path + ">")

        extension = os.path.splitext(path)[1]
        content_type = {
            ".html": "text/html",
            ".ico": "image/x-icon",
            ".css": "text/css",
            ".js": "application/javascript",
            ".svg": "image/svg+xml",
            ".map": "application/octet-stream",  # https://stackoverflow.com/a/19912684/473672
        }[extension]

        f = None
        try:
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return

        self.send_response(200)
        self.send_header("Content-type", content_type)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()

        shutil.copyfileobj(f, self.wfile)
        f.close()


# "0" gets us a random port: https://stackoverflow.com/a/442074/473672
server_address = ('localhost', 0)

httpd = BaseHTTPServer.HTTPServer(server_address, Handler)
url = "http://localhost:" + str(httpd.server_port)
print("Serving on " + url)

# Note that there's no race here; the port is already in LISTEN when we get
# here, and the web browser will simply wait until we start serving.
webbrowser.open(url)
httpd.serve_forever()
