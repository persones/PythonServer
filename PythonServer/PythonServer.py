# -*- coding: utf-8 -*-
"""
Created on Thu Jun 06 18:37:24 2013

@author: Person
"""
import BaseHTTPServer

class MyServer(BaseHTTPServer.HTTPServer):
    a = 1
    
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def dont_GET(s):
        """Respond to a GET request."""
        print s
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")  

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    print ('running ' + server_class.__name__ + " " +  handler_class.__name__)
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
run()