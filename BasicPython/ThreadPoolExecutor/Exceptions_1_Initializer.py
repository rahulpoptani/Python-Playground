# An exception can be raised from:
# 1. Initializer Function
# 2. From the task itself
# 3. From Callback

# Exception raised from Initialization function will break the thread pool

from time import sleep
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def initialize_worker():
    raise Exception('From Initializer')

def task(identifier):
    sleep(1)
    return identifier

with ThreadPoolExecutor(max_workers=2, initializer=initialize_worker) as executor:
    for result in executor.submit(task, range(10)):
        print(result)