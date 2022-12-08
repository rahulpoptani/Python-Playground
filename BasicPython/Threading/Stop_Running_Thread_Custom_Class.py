
import time
from threading import Thread
from threading import Event

class CustomClass(Thread):
    # constructor
    def __init__(self, event):
        # call parent constructor
        super(CustomClass, self).__init__()
        self.event = event
    # execute task
    def run(self):
        while True:
            # block for a moment. Blocking is important. It allows CPU to context switch to another thread. Sleep should be added even if it's for a fraction of second.
            time.sleep(1)
            if self.event.is_set():
                break
            print('Worker thread running...')
        print('Worker closing..')

# create event
event = Event()

# create new thread
thread = CustomClass(event)

# start thread
thread.start()

# block for a while
time.sleep(4)

print('Thread stopped by Main thread')
event.set()

# wait for the new thread to finish
thread.join()