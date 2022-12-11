# It allows multiple threads to wait on the same barrier object instance (e.g. at the same point in code) 
# until a predefined fixed number of threads arrive (e.g. the barrier is full), 
# after which all threads are then notified and released to continue their execution.
# Internally, a barrier maintains a count of the number of threads waiting on 
# the barrier and a configured maximum number of parties (threads) that are 
# expected. Once the expected number of parties reaches the pre-defined maximum, 
# all waiting threads are notified.

from time import sleep
from random import random
from threading import Thread
from threading import Barrier

def task(barrier: Barrier, number):
    value = random()*10
    sleep(value)
    print(f'Thread: {number} done; got: {value}')
    # wait on all other threads to complete
    barrier.wait()

# one additional for the main thread that will also wait for all threads to reach the barrier
barrier = Barrier(5+1)
for i in range(5):
    Thread(target=task, args=(barrier, i)).start()

print('Main thread waiting on all results...')
barrier.wait()
# alternate - this is required when you want your last thread to do some work after barrier is released
# remaining = barrier.wait()
# if remaining == 0:
#     print('Last Thread.')
print('All threads have thier result')
