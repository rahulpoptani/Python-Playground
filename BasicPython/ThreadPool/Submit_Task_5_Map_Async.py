# It yields one result returned from the given target function called with one item from a given iterable. 
# The map_async() method does not block while the function is applied to each item in the iterable, instead it returns a AsyncResult object from which the results may be accessed.

# map_async() does not block, it allows the caller to continue and retrieve the result when needed.
# A callback function can be called automatically if the task was successful, e.g. no error or exception.

from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier):
    value = random()
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return value

with ThreadPool() as pool:
    result = pool.map_async(task, range(10))
    for result in result.get():
        print(f'Got result: {result}')
    # alternate: result.wait() to wait for all task to complete inside context manager
