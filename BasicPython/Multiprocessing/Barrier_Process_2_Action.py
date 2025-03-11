# We can trigger an action once all parties reach the barrier.
# This can be achieved by setting the “action” argument to a callable in the multiprocessing.Barrier constructor.
# The callable could be a lambda or a function with no arguments.

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier

# action when all process reach barrier
def report():
    print('All process have result')

def task(barrier, number):
    value = random()
    sleep(value)
    print(f'Process {number}, got: {value}', flush=True)
    # wait for all other processes to completes
    barrier.wait()

if __name__ == '__main__':
    barrier = Barrier(5, action=report)    
    processes = [Process(target=task, args=(barrier,i)) for i in range(5)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
