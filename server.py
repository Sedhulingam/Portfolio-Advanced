import http.server
import socketserver

PORT = 3000

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_PUT(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        print("PUT data:", data)
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()