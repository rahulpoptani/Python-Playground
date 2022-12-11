# This function takes a callable, such as a function with no arguments 
# or a lambda expression. The thread calling the wait_for() function will 
# block until notified and the callable passed in as an argument returns a True value.
# This might mean that the thread is notified many times by different threads, 
# but will only unblock and continue execution once the condition in the callable is met.

from time import sleep
from random import random
from threading import Thread
from threading import Condition

def task(condition, work_list):
    # aquire condition
    with condition:
        value = random()
        sleep(value)
        work_list.append(value)
        print(f'Thread added {value}')
        # notify waiting thread
        condition.notify()

# create a condition
condition = Condition()
work_list = list()
# start few threads that will add wor to the list
for i in range(5):
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()

# wait for all threads to add thier work to the list
with condition:
    condition.wait_for(lambda: len(work_list) == 5)
    print(f'Done, got: {work_list}')