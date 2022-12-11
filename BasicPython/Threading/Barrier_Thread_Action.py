# We can trigger an action once all parties reach the barrier.
# The callable could be a lambda or a function with no arguments.

from time import sleep
from random import random
from threading import Thread
from threading import Barrier

# action once all threads reach the barrier
def report():
    # report once all theads are done
    print('All threads have thier result')

def task(barrier: Barrier, number):
    value = random()*10
    sleep(value)
    print(f'Thread: {number} done; got: {value}')
    # wait on all other threads to complete
    barrier.wait()


# Because the main thread no longer needs to wait on the barrier, 
# we can reduce the number of expected parties to reach the barrier to five, 
# to match the five worker threads
barrier = Barrier(5, action=report)
for i in range(5):
    Thread(target=task, args=(barrier, i)).start()

