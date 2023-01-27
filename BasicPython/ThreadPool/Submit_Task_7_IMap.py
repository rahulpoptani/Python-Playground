# The imap() method is a lazier version of them map() method where we submit tasks one-by-one to the ThreadPool and retrieve results for tasks as they complete

    # Items are yielded from the provided iterable one at a time instead of all at once.
    # Results are yielded in order as they are completed rather than after all tasks are completed.

# Difference Between imap() and map()
    # The imap() method issues one task at a time to the ThreadPool, the map() method issues all tasks at once to the pool.
    # The imap() method blocks until each task is complete when iterating the return values, the map() method blocks until all tasks complete when iterating return values.

# The imap() method should be used for issuing tasks one-by-one and handle the results for tasks in order as they are available.
# The map() method should be used for issuing all tasks at once and handle results in order only once all issued tasks have completed.

# Difference Between imap() and imap_unordered()
# The iterable returned from imap() yields results in order as they are completed, whereas the imap_unordered() method yields results in an arbitrary order in which tasks are completed.

from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier):
    value = random()
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return value

with ThreadPool(4) as pool:
    for result in pool.imap(task, range(40), chunksize=4):
        print(f'Got result: {result}')