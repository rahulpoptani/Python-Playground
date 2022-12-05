# share data between threads
# Data may refer as Global, Local or Instance variable
# it could be a counter, boolean or application specific Data Structure

# Problem: Multiple threads reading or writing same variable can result in concurrency failure mode called a race condition.

# Different methods to share data depends on the type of data shared:
# Sharing Boolean variable: threading.Event
# Protecting shared data: threading.Lock
# Sharing data: queue.Queue

import threading
from random import random
import time

# 1. Sharing a Boolean variable with an Event
# The threading.Event class ensures all access and change to boolean variable is thread safe, avoid race condition

def task(event: threading.Event, number):
    # wait for the event to be set
    event.wait()
    # begin processing
    value = random()
    time.sleep(value)
    print(f'Thread: {number} got value: {value}')


# create shared event object, not set by default
event = threading.Event()

# create multiple threads
for i in range(5):
    thread = threading.Thread(target=task, args=(event, i))
    thread.start()

# block main thread
print('Main thread blocking..')
time.sleep(2)
# start processing all threads
event.set()
# wait for all threads to finish

