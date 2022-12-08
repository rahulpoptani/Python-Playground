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
    # block for a moment
    time.sleep(random())
    # wait for data
    with condition:
        while True:
            print('Thread waiting on condition')
            # check the data
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
