# It yields one result returned from the given target function called with one item from a given iterable.
#  tasks are issued (and perhaps executed) in the same order as the results are returned.

# Difference Between map() and map_async()
    # The map() method blocks, whereas the map_async() method does not block.
    # The map() method returns an iterable of return values from the target function, whereas the map_async() function returns an AsyncResult.
    # The map() method does not support callback functions, whereas the map_async() method can execute callback functions on return values and errors.

from time import sleep
from random import random
from multiprocessing.pool import ThreadPool

def task(identifier):
    value = random()
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return value

with ThreadPool(4) as pool:
    # The map() function is called for the range with a chunksize of 10.
    # This issues 4 units of work to the ThreadPool, one for each worker thread and each composed of 10 calls to the task() function.
    for result in pool.map(task, range(40), chunksize=10):
        print(f'Got Result: {result}')