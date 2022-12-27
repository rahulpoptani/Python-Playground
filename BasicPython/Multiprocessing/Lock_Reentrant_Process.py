# A standard mutex lock does not allow a process to acquire the lock more than once. 
# This means that code in one critical section cannot call or execute code with another critical section protected by the same lock. 
# Instead, a different type of mutex lock is required called a reentrant lock.

# RLock allows a process (or thread) to acquire the lock more than once.

# We can imagine critical sections spread across a number of functions, each protected by the same lock. 
# A process may call across these functions in the course of normal execution and may call into one critical section from another critical section.

# A limitation of a (non-reentrant) mutex lock is that if a process has acquired the lock that it cannot acquire it again. 
# In fact, this situation will result in a deadlock as it will wait forever for the lock to be released so that it can be acquired, but it holds the lock and will not release it.

# A reentrant lock will allow a process to acquire the same lock again if it has already acquired it. 
# This allows the process to execute critical sections from within critical sections, as long as they are protected by the same reentrant lock.


from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import RLock

def report(lock, identifier):
    with lock:
        print(f'Process {identifier} done')

# Given that the target task function is protected with a lock and calls the reporting function that is also protected by the same lock, 
# we can use a reentrant lock so that if a process acquires the lock in task(), it will be able to re-enter the lock in the report() function.
def task(lock, identifier, value):
    with lock:
        print(f'Process {identifier} sleeping for {value}')
        sleep(value)
        report(lock, identifier)

if __name__ == '__main__':
    lock = RLock()
    processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()