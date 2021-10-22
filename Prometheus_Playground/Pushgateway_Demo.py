from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, registry

registry = CollectorRegistry()
g = Gauge('job_last_sucess_unix_time', 'Last time a batch job sucessfull finished', registry=registry)
g.set_to_current_time()
push_to_gateway('localhost:9091', job = 'batchA', registry=registry)
