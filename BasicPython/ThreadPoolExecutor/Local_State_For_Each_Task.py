# You can use thread local variables for worker threads in the ThreadPoolExecutor.

from time import sleep
from random import random
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait

def initializer_worker(local):
    local.key = random()
    print(f'Initializing worker thread: {local.key}')

def task(local):
    mykey = local.key
    sleep(mykey)
    return f'Worker using {mykey}'

local = threading.local()
executor = ThreadPoolExecutor(max_workers=2, initializer=initializer_worker, initargs=(local,))
futures = [executor.submit(task, local) for _ in range(10)]
for future in futures:
    result = future.result()
    print(result)
executor.shutdown()
print('done')