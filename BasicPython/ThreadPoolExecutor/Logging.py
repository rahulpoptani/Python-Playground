# logging library is thread-safe

import logging
from time import sleep
from concurrent.futures import ThreadPoolExecutor, wait

def task(number):
    sleep(0.5)
    logging.debug(f'Successfully completed task: {number}')
    return f'Task Done: {number}'

logging.basicConfig(level=logging.DEBUG)

with ThreadPoolExecutor(5) as executor:
    futures = [executor.submit(task, i) for i in range(50)]
    print('Waiting for task to complete')
    wait(futures)