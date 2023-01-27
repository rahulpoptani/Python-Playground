# There are many examples of why we may need to use threads within worker processes, such as:
    # Worker processes need to download data from the network or internet.
    # Worker processes need to save or load data to or from file.
    # Worker processes need to store or retrieve data from a database.

from random import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait

def thread_work(process_id, thread_id):
    sleep(random())
    print(f'Process: {process_id}, thread worker: {thread_id}', flush=True)

def process_work(identifer):
    with ThreadPoolExecutor() as texe:
        tfutures = [texe.submit(thread_work, identifer, i) for i in range(5)]
        _ = wait(tfutures)
    print(f'Process {identifer} done', flush=True)

if __name__ == '__main__':
    with ProcessPoolExecutor() as pexe:
        pfutures = [pexe.submit(process_work, i) for i in range(5)]
        _ = wait(pfutures)
    print('Main Done', flush=True)