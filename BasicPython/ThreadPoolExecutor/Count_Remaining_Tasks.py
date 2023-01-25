from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def task():
    sleep(random())

n_worker = 4
with ThreadPoolExecutor(max_workers=n_worker) as executor:
    futures = [executor.submit(task) for _ in range(15)]
    for _ in as_completed(futures):
        size = executor._work_queue.qsize() + n_worker
        print(f'About {size} remains')

# Another approach

with ThreadPoolExecutor(max_workers=n_worker) as executor:
    _ = [executor.submit(task) for _ in range(15)]
    while executor._work_queue.qsize() > 0:
        size = executor._work_queue.qsize() + n_worker
        print(f'About {size} remains')
        sleep(0.1)
    print(f'{n_worker} or fewer task remains')

# Another approach

TOTAL_TASK = 15
with ThreadPoolExecutor(max_workers=n_worker) as executor:
    futures = [executor.submit(task) for _ in range(TOTAL_TASK)]
    completed = 0
    for _ in as_completed(futures):
        completed += 1
        size = TOTAL_TASK - completed
        print(f'About {size} remains')

# Another approach via callback with lock and global variable