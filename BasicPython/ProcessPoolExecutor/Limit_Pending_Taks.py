from time import sleep
from random import random
from multiprocessing import Semaphore, Manager
from concurrent.futures import ProcessPoolExecutor

def work(identifier):
    sleep(random())
    print(f'Done: {identifier}')
    return identifier

def task_complete_callback(future):
    semaphore.release()

# The proxy submit() function would take the name of the target task function and 
# any arguments to that function, just like the submit() function on the Executor class (the parent class of the ProcessPoolExecutor).
def submit_proxy(function, *args, **kwargs):
    semaphore.acquire()
    future = executor.submit(function, *args, **kwargs)
    future.add_done_callback(task_complete_callback)
    return future

# The main process in the primary process is blocked after ten tasks are submitted and slowly adds new tasks as the initial tasks are completed and releases resources in the semaphore.
if __name__ == '__main__':
    n_workers = 2
    n_queue = 10
    with Manager() as manager:
        semaphore = manager.Semaphore(n_queue)
        with ProcessPoolExecutor(n_workers) as executor:
            futures = [submit_proxy(work, i) for i in range(50)]
            print(f'All tasks are submitted, waiting..')
