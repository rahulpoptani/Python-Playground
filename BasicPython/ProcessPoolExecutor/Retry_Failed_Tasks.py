from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor, as_completed

def work(identifier):
    sleep(random())
    if random() < 0.3:
        raise Exception(f'Lesser than 0.3 Exception: {identifier}')
    return f'Completed: {identifier}'

if __name__ == '__main__':
    with ProcessPoolExecutor(10) as executor:
        futures_to_data ={executor.submit(work, i):i for i in range(10)}
        retries = {}
        for future in as_completed(futures_to_data):
            if future.exception():
                data = futures_to_data[future]
                future = executor.submit(work, data)
                retries[future] = data
                print(f'Failure, retrying {data}')
            else:
                print(future.result())
        print('\nRetries:')
        for future in as_completed(retries):
            if future.exception():
                data = retries[future]
                print(f'Failure on retry: {data}, not trying anymore')
            else:
                print(future.result())