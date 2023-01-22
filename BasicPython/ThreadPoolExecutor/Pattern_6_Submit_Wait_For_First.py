from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_COMPLETED

def task(number):
    sleep(1)
    return number

executor = ThreadPoolExecutor(10)
futures = [executor.submit(task, i) for i in range(10)]
done, not_done = wait(futures, return_when=FIRST_COMPLETED)
# get the result from the first finished task
print(done.pop().result())
executor.shutdown(wait=False, cancel_futures=True)