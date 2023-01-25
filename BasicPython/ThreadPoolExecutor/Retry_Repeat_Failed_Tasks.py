# Repeat retry until succed

from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

def work(identifier):
    sleep(random())
    if random() < 0.3:
        raise Exception(f'Under value received exception: {identifier}')
    return f'Completed: {identifier}'

def retry(future, future_to_data, executor):
    data = future_to_data[future]
    retry = executor.submit(work, data)
    future_to_data[retry] = data
    return data

TASKS = 20
completed = 0

with ThreadPoolExecutor(TASKS) as executor:
    futures_to_data = {executor.submit(work, i): i for i in range(TASKS)}
    while completed < TASKS:
        for future in as_completed(futures_to_data):
            if future.exception():
                data = retry(future, futures_to_data, executor)
                print(f'Failure, retrying {data}')
            else:
                print(future.result())
                completed += 1
            futures_to_data.pop(future)