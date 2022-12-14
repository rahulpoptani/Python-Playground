# We may decide to stop a running thread due to:
# 1. The result from task is no longer required
# 2. The application is shutting down
# 3. The outcome from the task has gone astray

# A thread can be stop using a shared boolean variable such as threading.Event
# threading.Event is a thread safe boolean variable that can either be set or not set
# The event is created by default as 'not set' or False state

# Note: If you want to stop multiple threads then share the same event with all thread, once condition is met all thread will eventually stop

import time
import threading

# custom task function
def task(event: threading.Event):
    # execute the task in loop
    while True:
        # block for a moment
        time.sleep(1)
        # check to stop
        if event.is_set():
            break
        print('Worker thread running...')
    print('Worker closing...')

# create an event
event = threading.Event()

# create and configure new thread
thread = threading.Thread(target=task, args=(event,))

# start thread
thread.start()

# block for a while
time.sleep(3)

# stop the worker thread
print('Thread stopped by Main')
event.set()
# wait for the new thread to finish
thread.join()
