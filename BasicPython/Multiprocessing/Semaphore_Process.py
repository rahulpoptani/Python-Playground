# A semaphore is essentially a counter protected by a mutex lock, used to limit the number of processes that can access a resource.
# It is an extension of a mutual exclusion (mutex) lock that adds a count for the number of processes that can acquire the lock before additional processes will block. 
# Once full, new processes can only acquire access on the semaphore once an existing process holding the semaphore releases access.

# the semaphore maintains a counter protected by a mutex lock that is incremented each time the semaphore is acquired and decremented each time it is released.
# Some examples include:
    # Limiting concurrent socket connections to a server.
    # Limiting concurrent file operations on a hard drive.
    # Limiting concurrent calculations.


from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Semaphore

# Only 3 process will be able to execute in parallel. Others will wait until semaphore is releases by previous 3 process.
# Observe the print will come in a batch of 3
def task(semaphore, number):
    with semaphore:
        sleep(1)
        print(f'Process {number} sleeping')

if __name__ == '__main__':
    semaphore = Semaphore(3)
    processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
