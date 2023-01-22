# Worker thread can call a function before they start the processing
# This is called initialization function

# Note: ThreadPoolExecutor does not create all the worker threads up-dront when the thread pool is created.
# Instead, it will create worker threads just-in-time until the fixed number of worker threads specified when configuring the thread pool is created.

# If the initializer function is set, it is called for each worker thread as the thread is created.

from time import sleep
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def initializer_worker():
    name = current_thread().name
    print(f'Initializing worker thread: {name}')

def task(identifier):
    sleep(1)
    return identifier

with ThreadPoolExecutor(max_workers=2, initializer=initializer_worker) as executor:
    for result in executor.map(task, range(10)):
        print(result)
