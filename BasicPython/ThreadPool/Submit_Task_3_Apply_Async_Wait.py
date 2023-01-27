
from time import sleep
from multiprocessing.pool import ThreadPool

def task():
    print(f'Task Executing')
    print(f'Task Done')

pool = ThreadPool()
result = pool.apply_async(task)
result.wait()
pool.close()