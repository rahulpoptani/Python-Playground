import http.server
from prometheus_client import start_http_server, Histogram
import time

REQUEST_RESPONSE_TIME = Histogram(name='app_response_latency_seconds', documentation='Response latency in seconds', buckets=[0.1, 0.5, 1, 2, 3, 4, 5, 10])

APP_PORT = 8000
METRIC_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    @REQUEST_RESPONSE_TIME.time()
    def do_GET(self):
        # start_time = time.perf_counter() # Using decorator instead
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        # time_taken = time.perf_counter() - start_time  # Using decorator instead
        # REQUEST_RESPONSE_TIME.observe(time_taken)  # Using decorator instead

if __name__ == "__main__":
    start_http_server(METRIC_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()

