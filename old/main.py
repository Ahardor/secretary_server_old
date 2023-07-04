from http.server import BaseHTTPRequestHandler, HTTPServer
import dbcon
import json

db = dbcon.dbConnector()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(db.select().encode(encoding='UTF-8'))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(json.loads(post_data.decode('utf-8')))
        print(json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False))
        self.send_response(200)
        self.end_headers()
        if "get" in data:
            self.wfile.write(db.select(data["get"]).encode(encoding='UTF-8'))
        elif "put" in data:
            db.insert(data)
        return

server = HTTPServer(("localhost", 8000), RequestHandler)
server.serve_forever()