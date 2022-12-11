# A semaphore is essentially a counter protected by a mutex lock, used to limit the number of threads that can access a resource.
# It is an extension of a mutual exclusion (mutex) lock that adds a count for 
# the number of threads that can acquire the lock before additional threads will block.
# A semaphore provides a useful concurrency tool for limiting the number of threads that can access a resource concurrently. Some examples include:
    # Limiting concurrent socket connections to a server.
    # Limiting concurrent file operations on a hard drive.
    # Limiting concurrent calculations.

from time import sleep
from random import random
from threading import Thread
from threading import Semaphore

def task(semaphore: Semaphore, number):
    # attemp to aquire semaphore
    with semaphore:
        value = random()
        sleep(value)
        print(f'Thread {number} got {value}')

semaphore = Semaphore(2)
# All ten threads attempt to acquire the semaphore, but only two threads are granted positions at a time. 
# Each release of the semaphore (via the context manager) allows another thread to acquire a position and perform its calculation
for i in range(10):
    Thread(target=task, args=(semaphore, i)).start()
