# You can get a livelock if a thread cannot make progress because of another thread, but is not blocked as with a deadlock.
# The threads may both attempt to acquire a lock or series of locks at the same time, 
# detect that they are competing for the same resource, and then back-off. 
# This process is repeated and neither thread is able to make progress and are “locked”.

# Example:
# Thread 1: Acquires Lock1, checks Lock2 and back off if it is not free
# Thread 2: Acquires Lock2, checks Lock1 and back off if it is not free


from time import sleep
from threading import Lock, Thread

def task(number, lock1, lock2):
    # loop until the task is completed
    while True:
        # acquire the first lock
        with lock1:
            # wait a moment
            sleep(0.1)
            # check if second lock is available
            if lock2.locked():
                print(f'Task {number} cannot get the second lock, giving up...')
            else:
                # acquire lock2
                print(f'Task {number} made it, all done.')
                break

lock1 = Lock()
lock2 = Lock()
thread1 = Thread(target=task, args=(0, lock1, lock2))
thread2 = Thread(target=task, args=(1, lock2, lock1))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# don't run

