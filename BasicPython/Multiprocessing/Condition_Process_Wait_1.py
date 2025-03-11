# we may need processes to wait for some condition within a critical section before continuing.
# This could be achieved using a mutual exclusion lock to protect the critical section, but the processes waiting for the condition would have to spin (execute in a loop) repeatedly releasing/re-acquiring the mutex lock until the condition was met.
# An alternative is to use a condition (also called a monitor) that builds upon a mutex and allows processes to wait and be notified.

# In concurrency, a condition (also called a monitor) allows multiple processes (or threads) to be notified about some result.
# It combines both a mutual exclusion lock (mutex) and a conditional variable.

# A condition can be acquired by a process (like a mutex) after which it can wait to be notified by another process that something has changed. 
# While waiting, the process is blocked and releases the lock for other processes to acquire.

# Another process can then acquire the condition, make a change, and notify one, all, or a subset of processes waiting on the condition that something has changed. 
# The waiting process can then wake-up, re-acquire the condition (mutex), perform checks on any changed state and perform required actions.

# Default condition creates a RLock

from time import sleep
from multiprocessing import Process
from multiprocessing import Condition

# condition = Condition()
# with condition:
#     condition.wait() # will wait forever
#     condition.wait(timeout=10) # will wait for 10 seconds
#     condition.wait_for(lambda x: x == 2) # takes function which returns Boolean and will only unlock the waiting process if condition is met
#     condition.notify() # notify a single waiting process
#     condition.notify(n=3) # notify a subset of waiting process.
#     condition.notify_all() # notify all waiting process

def task(condition):
    sleep(1)
    print(f'Child process sending notification..', flush=True)
    with condition:
        condition.notify()
    # do something else
    sleep(1)
    print('End of Child Process')

if __name__ == '__main__':
    condition = Condition()
    print('Main process waiting for data..')
    with condition:
        worker = Process(target=task, args=(condition,))
        worker.start()
        condition.wait()
    print('Main process all done')
