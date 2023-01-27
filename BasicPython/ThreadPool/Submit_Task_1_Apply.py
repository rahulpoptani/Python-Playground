# The apply() method takes the name of the function to execute by a worker thread. 
# The call will block until the function is executed by a worker thread, after which time it will return.

# the capabilities of the apply() method are as follows:
    # Issues a single task to the ThreadPool.
    # Supports multiple arguments to the target function.
    # Blocks until the call to the target function is complete.

# Difference Between apply() vs apply_async()
    # The apply() method blocks, whereas the apply_async() method does not block.
    # The apply() method returns the result of the target function, whereas the apply_async() method returns an AsyncResult.
    # The apply() method does not take callbacks, whereas the apply_async() method does take callbacks.

from time import sleep
from random import random
from multiprocessing.pool import ThreadPool

def task(data):
    value = random()
    print(f'Task Executing: {data}')
    sleep(value)
    print(f'Task Done: {data}')
    return value

pool = ThreadPool()
result = pool.apply(task, args=('Hello',))
print(f'Main got: {result}')
pool.close()