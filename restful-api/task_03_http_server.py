#!/usr/bin/python3
"""This module contains restful-api tasks."""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class RequestHandler(BaseHTTPRequestHandler):
    """class RequestHandler"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(f"{json.dumps(response)}".encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))            


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server started at http://localhost:8000")
    server.serve_forever()
