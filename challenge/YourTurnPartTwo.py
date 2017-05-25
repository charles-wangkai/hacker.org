#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=55
# A: (Not fixed answer, submit the URL hosting this running script)

import http.server
import socketserver
import urllib.parse

values = set()

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parse_result = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parse_result.query)
        
        self.send_response(200)
        self.end_headers()
            
        command = next(iter(query.keys()))
        value = query[command][0]
        
        if command == 'set':
            values.add(value)
        else:
            self.wfile.write(('yes' if value in values else 'no').encode())

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

def serve_httpd():
    httpd = ThreadedHTTPServer(('', 8888), MyRequestHandler)
    sa = httpd.socket.getsockname()

    print('Serving HTTP on %s port %d ...' % (sa[0], sa[1]))
    httpd.serve_forever()

def main():
    serve_httpd()

if __name__ == '__main__':
    main()
