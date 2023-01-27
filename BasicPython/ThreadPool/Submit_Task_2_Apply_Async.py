# Asynchronous means that the call to the ThreadPool does not block, allowing the caller that issued the task to carry on.

# the capabilities of the apply_async() method are as follows:
    # Issues a single task to the ThreadPool.
    # Supports multiple arguments to the target function.
    # Does not block, instead returns a AsyncResult.
    # Supports callback for the return value and any raised errors.

from time import sleep
from random import random
from multiprocessing.pool import ThreadPool

def return_callback(result):
    print(f'Callback Received: {result}')

def error_callback(error):
    print(f'Received Exception: {error}')

def task(data):
    value = random()
    if value < 0.3:
        raise Exception('Less than 0.3 Exeption')
    print(f'Task Executing: {data}')
    sleep(value)
    print(f'Task Done: {data}')
    return value

pool = ThreadPool()
pool.apply_async(task, args=('Hello',), callback=return_callback, error_callback=error_callback)
pool.close()
pool.join()
