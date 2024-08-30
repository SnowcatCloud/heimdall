import http.server
import socketserver
import re

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        origin = self.headers.get('Origin')
        
        self.send_header('Access-Control-Allow-Origin', 'https://previewfp.snowcatcloud.com,https://customerioforms.com/,http://localhost:3000')
        #self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        # self.send_header('Access-Control-Allow-Headers', '*')
        # self.send_header('Access-Control-Allow-Credentials', 'true')

        # Your other custom headers
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '600')
        self.send_header('Accept-Ch', 'Sec-CH-UA, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Full-Version, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform, Sec-CH-UA-Platform-Version, Sec-CH-UA-WoW64')

        # Add other CORS headers
        # self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        # self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        
        super().end_headers()

# Server setup
PORT = 3000

with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
