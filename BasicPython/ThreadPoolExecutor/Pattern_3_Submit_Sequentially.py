# We may require the result sequentially
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def task(number):
    sleep(1)
    return number

with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in futures:
        print(future.result())