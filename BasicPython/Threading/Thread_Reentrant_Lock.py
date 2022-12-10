# A reentrant lock is a lock that can be acquired more than once by the same thread.

from time import sleep
from random import random
from threading import Thread
from threading import RLock

# reporting function
def report(lock, identifier):
    # aquire the lock:
    with lock:
        print(f'thread {identifier} done')

# work function
def task(lock, identifier, value):
    # aquire the lock
    with lock:
        print(f'thread {identifier} sleeping for {value}')
        sleep(value)
        # report
        report(lock, identifier)

# create shared reentrant lock
lock = RLock()
# start few threads that attempt to execute the same critical section
for i in range(10):
    Thread(target=task, args=(lock, i, random())).start()

# Only one thread can acquire the lock at a time, and then once acquired, blocks and then reenters the same lock again to report the done message.


