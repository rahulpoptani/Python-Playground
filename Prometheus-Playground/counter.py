import http.server
from prometheus_client import start_http_server, Counter

# Define Counter
REQUEST_COUNT = Counter(name='app_requests_total', documentation='total all http request counts', labelnames=['app_name', 'endpoint'])

APP_PORT = 8000
METRIC_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_COUNT.labels('prom_python_app', self.path).inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRIC_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()

