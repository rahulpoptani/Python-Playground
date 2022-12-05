# If we want a thread to start executing our code after a time limit has expired.

import threading
import time 

def task(argument):
    print(f'This will run after configured seconds: dummy argument: {argument}')

# configure timer thread
# the target task function WILL NOT execute until the time has elapsed
timer = threading.Timer(3, task, args=('something',))

# start timer object
timer.start()
print('This will run immediately')

# if we want to cancel the thread before the timer has expired
# timer.cancel()