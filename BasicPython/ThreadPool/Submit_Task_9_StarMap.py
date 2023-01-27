# The ThreadPool provides a version of map() that permits multiple arguments to the target task function via the starmap() method.

# Difference Between starmap() and map()
# starmap() method and the map() method is that starmap() supports a target function with more than one argument, whereas the map() method supports target functions with only one argument.

# Difference Between starmap() and starmap_async()
    # The starmap() method blocks, whereas the starmap_async() method does not block.
    # The starmap() method returns an iterable of return values from the target function, whereas the starmap_async() method returns an AsyncResult.
    # The starmap() method does not support callback functions, whereas the starmap_async() method can execute callback functions on return values and errors.

from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier, value):
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return (identifier, value)

with ThreadPool(4) as pool:
    items = [(i, random()) for i in range(50)]
    for result in pool.starmap(task, items, chunksize=4):
        print(f'Got Result: {result}')