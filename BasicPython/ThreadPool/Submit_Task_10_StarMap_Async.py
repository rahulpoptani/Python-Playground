# The ThreadPool provides an asynchronous version of the starmap() method via the starmap_async() method.

from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier, value):
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return (identifier, value)

with ThreadPool(4) as pool:
    items = [(i, random()) for i in range(50)]
    result = pool.starmap_async(task, items, chunksize=4)
    for result in result.get():
        print(f'Got result: {result}')