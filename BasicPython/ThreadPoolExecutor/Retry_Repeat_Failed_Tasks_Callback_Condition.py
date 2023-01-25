from random import random
from time import sleep
from threading import Lock, Condition
from concurrent.futures import ThreadPoolExecutor, as_completed

def work(identifier):
    sleep(random())
    if random() < 0.3:
        raise Exception(f'Under value received exception: {identifier}')
    return f'Completed: {identifier}'

def auto_retry(future):
    global executor, futures_to_data, task_completed
    if future.exception():
        data = futures_to_data[future]
        retry = executor.submit(work, data)
        futures_to_data[retry] = data
        retry.add_done_callback(auto_retry)
        print(f'Failure, retrying.. {data}')
    else:
        print(future.result())
        with lock:
            task_completed += 1
            if task_completed >= TASKS:
                with condition:
                    condition.notify()

TASKS = 20
task_completed = 0
lock = Lock()
condition = Condition()

with ThreadPoolExecutor(TASKS) as executor:
    futures_to_data = {executor.submit(work, i): i for i in range(TASKS)}
    for future in futures_to_data:
        future.add_done_callback(auto_retry)
    # block wait until all task completed successfully
    with condition:
        condition.wait()