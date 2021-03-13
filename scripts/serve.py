#!/usr/bin/python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.chdir("../data")
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        # self.send_header('Access-Control-Allow-Methods', 'GET')
        # self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()
server = HTTPServer(('', 8003), CORSRequestHandler)
server.serve_forever()
