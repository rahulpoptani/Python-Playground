# We can use a manager to share a semaphore among workers in the multiprocessing pool.
# Like all concurrency primitives, the semaphore cannot be pickled.

# This is a problem when using the multiprocessing.Pool class to execute an ad hoc function because all arguments to tasks in the pool must be pickled.
# This will raise runtime exception when trying with Pool class, instead use Manager

from time import sleep
from random import random
from multiprocessing import Pool, Manager

def task(number, semaphore):
    with semaphore:
        value = random()
        sleep(value)
        print(f'{number} got {value}', flush=True)

if __name__ == '__main__':
    with Manager() as manager:
        semaphore = manager.Semaphore(4)
        with Pool() as pool:
            args = [(i, semaphore) for i in range(16)]
            pool.starmap(task, args)