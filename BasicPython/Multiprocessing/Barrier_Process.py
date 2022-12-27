# we may need to coordinate action between two or more processes.
# One way to achieve coordination is to have process reach and wait upon a barrier until all processes arrive, after which an action can be performed.

# It allows multiple processes (or threads) to wait on the same barrier object instance (e.g. at the same point in code) until a predefined fixed number of processes arrive (e.g. the barrier is full), 
# after which all processes are then notified and released to continue their execution.

# Internally, a barrier maintains a count of the number of processes waiting on the barrier and a configured maximum number of parties (processes) that are expected. 
# Once the expected number of parties reaches the pre-defined maximum, all waiting processes are notified.

# Barrier(4, action=python_callable_function) # the action will be callable that does not take argument and will be executed by one process once all process reach barrier
# barrier.abort() # if you wish to cancel the coordination
# barrier.reset() # if you cancel a coordination effort although you wish to retry it again with the same barrier instance

# Finally, the status of the barrier can be checked via attributes.
    # parties: reports the configured number of parties that must reach the barrier for it to be lifted.
    # n_waiting: reports the current number of processes waiting on the barrier.
    # broken: attribute indicates whether the barrier is currently broken or not.

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier

def task(barrier, number):
    value = random()
    sleep(value)
    print(f'Process {number}, got: {value}', flush=True)
    # wait for all other processes to complete
    barrier.wait()

if __name__ == '__main__':
    barrier = Barrier(5+1) 
    # Start 5 process that will wait on the barrier
    for i in range(5):
        worker = Process(target=task, args=(barrier,i))
        worker.start()
    print(f'Main process waiting on all results..')
    # Main will be the 6th one to wait. Hence the barrier is broken now
    barrier.wait()
    print('All process have result')