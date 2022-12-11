# the main thread can wait a fixed number of seconds for all threads to finish. 
# If all threads finish within the time, all is well, otherwise 
# we can report that not all work could be finished on time.
# When using a timeout, all calls to wait() should handle a potential BrokenBarrierError that could be raised.

from time import sleep
from random import random
from threading import Thread
from threading import Barrier, BrokenBarrierError

def task(barrier: Barrier, number):
    value = random()*10
    sleep(value)
    print(f'Thread: {number} done; got: {value}')
    # wait on all other threads to complete
    try:
        barrier.wait()
    except BrokenBarrierError:
        pass

barrier = Barrier(5+1)
for i in range(5):
    Thread(target=task, args=(barrier, i)).start()

print('Main thread waiting on all results...')
try:
    barrier.wait(timeout=5)
    print('All threads have thier result')
except:
    print('Some thread did not finish on time..')
