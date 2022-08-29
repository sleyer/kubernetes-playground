from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class HelloWorldServer(BaseHTTPRequestHandler):
    response_data = open("response.html").read()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.response_data, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), HelloWorldServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")