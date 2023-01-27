from random import random
from time import sleep
from multiprocessing.pool import ThreadPool

def custom_callback(result):
    print(f'Callback result: {result}')

def error_callback(error):
    print(f'Callback Exception: {error}')

def task(identifier):
    value = random()
    if value < 0.3:
        raise Exception(f'Got less than 0.3 exception: {value}')
    print(f'Task {identifier} executing with {value}')
    sleep(value)
    return value

with ThreadPool() as pool:
    _ = pool.map_async(task, range(10), callback=custom_callback, error_callback=error_callback)
    pool.close()
    pool.join()

# Note: it will stop at first exception