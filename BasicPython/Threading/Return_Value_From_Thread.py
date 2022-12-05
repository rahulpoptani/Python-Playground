# When using thread, we need to return a value from the thread to another thread:
# 1. The new thread loaded some data that needs to be returned
# 2. The new thread calculated something that needs to be returned
# 3. The new thread needs to share it states or status with another thread

import time
from threading import Thread

class CustomClass(Thread):
    # execute base constructor
    def __init__(self):
        Thread.__init__(self)
        # set default value
        self.value = None
    # function executed in new thread
    def run(self):
        time.sleep(1)
        # store data in instance variable
        self.value = 'Hello from a new thread'

# creat thread
thread = CustomClass()
# start thread
thread.start()
# wait for thread to finish
thread.join()
# get returned value from thread
data = thread.value
print(data)