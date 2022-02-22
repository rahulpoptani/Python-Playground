import http.server
from prometheus_client import start_http_server, Gauge
import time

REQUEST_INPROGRESS = Gauge(name='app_requests_inprogress', documentation='Number of application requests in total')
REQUEST_LASTSERVED = Gauge(name='app_last_served', documentation='Time the application was last served')

APP_PORT = 8000
METRIC_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    @REQUEST_INPROGRESS.track_inprogress()
    def do_GET(self):
        # REQUEST_INPROGRESS.inc()  #above decorator will take care of increment and decrement
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        REQUEST_LASTSERVED.set_to_current_time()
        # REQUEST_LASTSERVED.set(time.time()) # inbuilt method will take care of seting the time explicitly
        # REQUEST_INPROGRESS.dec()

if __name__ == "__main__":
    start_http_server(METRIC_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()

