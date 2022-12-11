# We might want to abort the coordination of threads on the barrier for some reason.
# We can abort the barrier by calling the abort() function, this will cause all threads 
# waiting on the barrier to raise a BrokenBarrierError and all new callers to wait() to raise the same error.
# This means that all calls to wait() should be protected by a try-except structure.

#  We will add a check in the thread processing task that if a value larger than 8 
# is encountered, abort the coordination effort, otherwise proceed.
# This means sometimes all threads will coordinate and sometimes not, depending on the specific random numbers generated.

from time import sleep
from random import random
from threading import Thread
from threading import Barrier, BrokenBarrierError

def task(barrier: Barrier, number):
    value = random()*10
    sleep(value)
    print(f'Thread: {number} done; got: {value}')
    if value > 8:
        print(f'Thread {number} aborting')
        barrier.abort()
    else:
        try:
            barrier.wait()
        except BrokenBarrierError:
            pass

barrier = Barrier(5+1)
for i in range(5):
    Thread(target=task, args=(barrier, i)).start()

print('Main thread waiting on all results...')
try:
    barrier.wait()
except BrokenBarrierError:
    print('At least one thread aborted due to bad result..')

