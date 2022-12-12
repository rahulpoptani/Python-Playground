
# There are many possibilities for a deadlock, one of them is
# Aquiring the same lock twice by same thread

# Common examples of the cause of threading deadlocks include:
    # A thread that waits on itself (e.g. attempts to acquire the same mutex lock twice).
    # Threads that wait on each other (e.g. A waits on B, B waits on A).
    # Thread that fails to release a resource (e.g. mutex lock, semaphore, barrier, condition, event, etc.).
    # Threads that acquire mutex locks in different orders (e.g. fail to perform lock ordering).

# Tips to avoid deadlock
# 1. Use Context Manager
# 2. Use timeout when waiting
# 3. Always acquire lock in the same order

from threading import Thread, Lock

# task2 to be executed in a new thread
def task2(lock):
    print('Thread aquiring lock again..')
    with lock:
        pass

# task1 to be executed in a new thread
def task(lock):
    print('Thread acquiring lock...')
    with lock:
        task2(lock)

# create a mutex lock
lock = Lock()
# create and configured new thread
thread = Thread(target=task, args=(lock,))
thread.start()
# wait for thread to exit. This will never happen as we reached deadlock
thread.join()

