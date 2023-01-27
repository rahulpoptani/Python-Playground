from time import sleep
from multiprocessing.pool import ThreadPool
from threading import current_thread

def task():
    thread = current_thread()
    print(f'Worker executing task, thread = {thread.name}')
    sleep(1)

def initialize_worker():
    thread = current_thread()
    print(f'Initializing Worker, thread = {thread.name}')

with ThreadPool(2, initializer=initialize_worker) as pool:
    for _ in range(4):
        _ = pool.apply_async(task)
    pool.close()
    pool.join()