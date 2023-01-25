# we must know what argument were passed to the task in order to re submit the task with same argument

from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

def work(identifier):
    sleep(random())
    if random() < 0.3:
        raise Exception(f'Under value received exception: {identifier}')
    return f'Completed: {identifier}'

with ThreadPoolExecutor(10) as executor:
    # submit 10 task - and store the future->data mapping
    futures_to_data = {executor.submit(work, i): i for i in range(10)}
    retries = {}
    for future in as_completed(futures_to_data):
        if future.exception():
            # if exception then retrive the data shared with the task
            data = futures_to_data[future]
            # submit the task again
            future = executor.submit(work, data)
            retries[future] = data
            print(f'Failure, retrying {data}')
        else:
            print(future.result())
    print('\nRetries')
    for future in as_completed(retries):
        if future.exception():
            data = retries[future]
            print(f'Failure on retry: {data}, not trying again')
        else:
            print(future.result())