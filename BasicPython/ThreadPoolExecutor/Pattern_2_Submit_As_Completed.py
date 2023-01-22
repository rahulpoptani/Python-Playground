from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def task(number):
    sleep(1)
    return number

with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in as_completed(futures):
        print(future.result())