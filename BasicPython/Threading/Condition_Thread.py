# A condition allows threads to wait and be notified
# It combines both a mutual exclusion lock (mutex) and a conditional variable.
# A condition can be acquired by a thread (like a mutex) after which 
# it can wait to be notified by another thread that something has changed. 
# While waiting, the thread is blocked and releases the lock for other threads to acquire.
# Another thread can then acquire the condition, make a change, 
# and notify one, all, or a subset of threads waiting on the condition 
# that something has changed. The waiting thread can then wake-up, 
# re-acquire the condition (mutex), perform checks on any changed state 
# and perform required actions.


from time import sleep
from threading import Thread
from threading import Condition

# The function will block for a moment, 
# add data to the list, then notify the waiting thread.
def task(condition, work_list):
    # block for a moment
    sleep(1)
    # add data to work list
    work_list.append(33)
    # notify a waiting thread that the work is done
    print('Thread sending notification...')
    with condition:
        # we cannot specify which thread to notify
        condition.notify()
        # condition.notify(n=3) # notify 3 waiting threads
        # condition.notify_all() # noify all waiting threads

# create condition
condition = Condition()
# prepare work list
work_list = list()
# wait to be notified that the data is ready
# Note, we must start the new thread after we have acquired the mutex lock in the condition in this example.
# If we did not acquire the lock first, it is possible that there would be a race condition. 
# Specifically, if we started the new thread before acquiring the condition and 
# waiting in the main thread, then it is possible for the new thread to execute 
# and notify before the main thread has had a chance to start waiting. 
# In which case the main thread would wait forever to be notified.
print('Main thread waiting for data...')
with condition:
    # start new thread and perform the task
    # Important: Start new thread only after aquiring mutex lock (condition)
    # This case is different: main is waiting for notification. If it was reverse, threads are waiting for notification than thread can be creation outside condition
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()
    # wait to be notified
    condition.wait()
    # alternate wait
    # condition.wait(timeout=2) # will wait only till configured seconds
# we know the data is ready
print(f'Got data {work_list}')