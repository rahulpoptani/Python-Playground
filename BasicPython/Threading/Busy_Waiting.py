# Busy waiting refers to a thread that repeatedly checks a condition in a loop.
# Busy waiting is typically undesirable in concurrent programming as the tight loop of checking condition consumes CPU cycles unnecessarily, occupying CPU core.
# That being said, there are some occasions where a busy wait is preferred.

import time
from random import random
from threading import Thread
from threading import Condition
from typing import List

# target functions
def task(condition: Condition, data: List):
    # Sleep will allow the operating system to context switch to another thread, possibly freeing up a CPU core
    time.sleep(random())
    # wait for data
    # allows the thread to respond to data changes directly, and/or to notification signals.
    with condition:
        # While loop should only go inside condition and NOT vice versa or else it will consume too many CPU Cycles
        while True:
            print('Thread waiting on condition')
            # check the data manually
            if len(data) > 0:
                break
            else:
                # timeout help not to wait forever and perform a manual check of condition
                condition.wait(timeout=0.2)
    print(f'Thread got data {data}')

# create the condition
condition = Condition()

# create data storage
data = list()

# create thread
thread = Thread(target=task, args=(condition, data))

# start the thread
thread.start()

# block for a moment
time.sleep(random())

# aquire the condition
with condition:
    # store the data
    data.append('Inserted This')
    # notify waiting thread
    print('Main thread is notifying..')
    condition.notify_all()
