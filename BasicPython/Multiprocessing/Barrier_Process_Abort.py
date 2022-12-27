# We might want to abort the coordination of processes on the barrier for some reason.
# This might be because one of the processes is unable to perform its required task.
# We can abort the barrier by calling the abort() function, this will cause all processes waiting on the barrier to raise a BrokenBarrierError and all new callers to wait() to raise the same error.

from time import sleep
from random import random
from multiprocessing import Barrier, Process
from threading import BrokenBarrierError

def task(barrier, number):
    value = random()*10
    sleep(value)
    print(f'Process {number} done, got: {value}', flush=True)
    if value > 7:
        print(f'Process {number} aborting..', flush=True)
        barrier.abort()
    else:
        try:
            barrier.wait()
        except BrokenBarrierError:
            print(f'Process: {number} Broken Barrier Exception')

if __name__ == '__main__':
    barrier = Barrier(5+1)
    for i in range(5):
        worker = Process(target=task, args=(barrier,i))
        worker.start()
    print('Main process waiting on all threads')
    try:
        barrier.wait()
        print('All process have thier results')
    except BrokenBarrierError:
        print('At least one process aborted due to bad result')