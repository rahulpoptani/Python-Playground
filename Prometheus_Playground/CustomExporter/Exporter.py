from typing import Counter
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, CounterMetricFamily, GaugeMetricFamily
import json, requests, time

EXPORTER_PORT = 8001
SERVER = 'http://localhost:8000'

class CustomCollector(object):
    def __init__(self, endpoint):
        self._endpoint = endpoint
    
    def collect(self):
        response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))
        
        yield CounterMetricFamily('visitors_server_total', 'App visitors server total', value=response['visitors_server'])

        traffic_metric = GaugeMetricFamily('traffic_channel', 'Traffic Channel Source', labels=['source'])
        for k, v in response['traffic_channel'].items():
            traffic_metric.add_metric([k], value=v)
        yield traffic_metric

if __name__ == "__main__":
    start_http_server(EXPORTER_PORT)
    REGISTRY.register(CustomCollector(SERVER))
    while True:
        time.sleep(1)

