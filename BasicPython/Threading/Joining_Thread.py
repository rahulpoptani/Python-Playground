# we may need to wait until another thread has finished running. 
# This may be for many reasons, such as:
# 1. The current thread needs a result from the target thread.
# 2. A resource is shared between the current and target threads
# 3. The current thread has no other work to complete.

# The join() method provides a way for one thread to block until another thread has finished.
# Once the target thread has finished, the join() method will return 
# and the current thread can continue to execute.

# The join() method also takes a “timeout” argument that specifies how long the current thread 
# is willing to wait for the target thread to terminate, in seconds.

from time import sleep
from threading import Thread

def task():
    # block for a moment
    sleep(1)
    # repor a message
    print('All done in new thread')

# create thread
thread = Thread(target=task)
# start thread
thread.start()
# wait for the new thread to finish
print('Main: Waiting for new thread to terminate')
thread.join()
# continue on
print('Main: Continuing on')