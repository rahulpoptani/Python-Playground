# the main process can wait a fixed number of seconds for all processes to finish. 
# If all processes finish within the time, all is well, otherwise we can report that not all work could be finished on time.

from time import sleep
from random import random
from multiprocessing import Barrier, Process
from threading import BrokenBarrierError

# All process will eventually raise exception as some might not be able to complete on time. Hence exception is raised by all process. 
# Changing 'value' to a lower number will easily give enough to for all to complete.
def task(barrier,number):
    value = random() * 10
    sleep(value)
    print(f'Process {number} done got {value}', flush=True)
    try:
        barrier.wait()
    except BrokenBarrierError:
        print(f'Process {number} Got Broken Barrier Exception..')

if __name__ == '__main__':
    barrier = Barrier(5+1)
    for i in range(5):
        worker = Process(target=task, args=(barrier,i))
        worker.start()
    print('Main process waiting on all threads')
    try:
        barrier.wait(timeout=5)
        print('All process have thier results')
    except BrokenBarrierError:
        print('Some process did not finish on time')
