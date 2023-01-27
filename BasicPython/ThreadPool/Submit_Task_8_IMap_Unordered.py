# The imap_unordered() method returns an iterable over the return values from each call to the target function. The iterable will yield return values as tasks are completed, in the order that tasks were completed, not the order they were issued.

# the capabilities of the imap_unordered() method are as follows:
    # Issue multiple tasks to the ThreadPool, one-by-one.
    # Returns an iterable over return values.
    # Supports a single argument to the target function.
    # Blocks until each task is completed in the order they are completed.
    # Allows tasks to be grouped and executed in batches by workers.

from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier):
    value = random()
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return value

with ThreadPool(4) as pool:
    for result in pool.imap_unordered(task, range(40), chunksize=4):
        print(f'Got result: {result}')