# A mutual exclusion lock or mutex lock is a synchronization primitive intended to prevent a race condition.
# An instance of the lock can be created and then acquired by processes before accessing a critical section, and released after the critical section.
# Only one process can have the lock at any time. If a process does not release an acquired lock, it cannot be acquired again.
# The process attempting to acquire the lock will block until the lock is acquired, such as if another process currently holds the lock then releases it.


# We can attempt to acquire the lock without blocking by setting the “blocking” argument to False. 
# lock.acquire(blocking=False)

# We can also attempt to acquire the lock with a timeout, that will wait the set number of seconds to acquire the lock before giving up.
# lock.acquire(timeout=10)


from time import sleep
from random import random
from multiprocessing import Process, Lock

#  the critical section involves reporting a message and blocking for a fraction of a second.
def task(lock, identifier, value):
    with lock:
        print(f'Process {identifier} got the lock, sleeping for {value}')
        sleep(value)

if __name__ == '__main__':
    lock = Lock()
    # Each process will receive the shared lock as an argument
    processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

