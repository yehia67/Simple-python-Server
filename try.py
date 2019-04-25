import http.server
import socketserver

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        print("serving at port", PORT)
        httpd.serve_forever()
    except IOError:
                    print "\nHTTP/1.1 404 Not Found\n\n"
