# In concurrency programming, we may want to perform actions while waiting for a lock to become available. 
# Waiting for a mutex lock in a loop is called a spinlock.

# A spinlock is a busy wait for a mutual exclusion (mutex) lock.
# Busy waiting, also called spinning, refers to a thread that repeatedly checks a condition.

# It is referred to as “busy” or “spinning” because the thread continues to execute the same code, such as an if-statement within a while-loop, achieving a wait by executing code (e.g. keeping busy).
    # Busy Wait: When a thread “waits” for a condition by repeatedly checking for the condition in a loop.

# A spinlock is a type of lock where a thread must perform a busy wait if it is already locked.
    # Spinlock: Using a busy wait loop to acquire a lock.


# In this example, we will set up the situation where the main thread creates a lock then creates and starts a new thread that attempts to acquire the lock using a spinlock. 
# The new thread will introduce a delay before attempting to acquire the lock. 
# In this delay, the main thread itself will acquire and hold the lock, causing the new thread to execute a busy wait loop of the spinlock for many iterations before finally acquiring the lock.

from time import sleep
from threading import Thread, Lock

def task(lock: Lock):
    sleep(0.5)
    while True:
        print('Thread trying to aquire the lock')
        # timeout reduces computation burden
        acquired = lock.acquire(blocking=True, timeout=0.5) # timeout if better than adding sleep, because there will not be a delay between the lock being available and the new thread acquiring it as there is with using a sleep.
        if acquired:
            print('Thread got the lock.. Finally')
            lock.release()
            break


lock = Lock()
Thread(target=task, args=(lock,)).start()
print('Main aquiring lock..')
with lock:
    sleep(5)
    print('Main all done')