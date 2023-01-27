
from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def task(identifier, value):
    if value < 0.3:
        raise Exception('Less than 0.3 Exception')
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return (identifier, value)

def custom_callback(result):
    print(f'Callback got value: {result}')

def error_callback(error):
    print(f'Callback Exception: {error}')

with ThreadPool(4) as pool:
    items1 = [(i, random()) for i in range(10)]
    _ = pool.starmap_async(task, items1)
    items2 = [(i, random()) for i in range(11,20)]
    _ = pool.starmap_async(task, items2, callback=custom_callback, error_callback=error_callback)
    pool.close()
    pool.join()