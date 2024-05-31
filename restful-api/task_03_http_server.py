#!/usr/bin/python3
import http.server  # Import the http.server module for creating an HTTP server
import json  # Import the json module for handling JSON data


# Create a subclass of http.server.BaseHTTPRequestHandler to handle requests
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Check the path of the request to route it to the appropriate handler
        if self.path == '/':
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as text/plain
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Write the response body
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as application/json
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Create a sample JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            # Write the JSON response body
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Send a 200 OK response
            self.send_response(200, message="OK")
            # Specify the content type as application/json
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Create a status JSON data
            status = {"status": "OK"}
            # Write the JSON response body
            self.wfile.write(json.dumps(status).encode('utf-8'))

        elif self.path == '/info':
            # Send a 200 OK response
            self.send_response(200)
            # Specify the content type as application/json
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Create an info JSON data
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            # Write the JSON response body
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Send a 404 Not Found response for undefined endpoints
            self.send_error(404, message="Not Found", explain="Endpoint not found")
            # Specify the content type as application/json
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            

# Set the server address and port
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print("Starting server on port 8000...")
httpd.serve_forever()
