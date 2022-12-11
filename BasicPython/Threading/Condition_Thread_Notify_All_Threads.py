# notify all threads waiting on a condition.

from time import sleep
from random import random
from threading import Thread
from threading import Condition

def task(condition: Condition, number):
    # wait to be notified
    print(f'Thread {number} waiting...')
    with condition:
        condition.wait()
    # block for a moment
    value = random()
    sleep(value)
    # report the result
    print(f'Thread {number} got {value}')

# create condition in main
condition = Condition()
# start few threads that will wait to be notified
for i in range(5):
    worker = Thread(target=task, args=(condition, i))
    worker.start()
# block for a moment
sleep(1)
# notify all waiting threads that they can run
with condition:
    condition.notify_all()

