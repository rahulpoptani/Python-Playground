from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED

def task(name):
    sleep(random())
    return name

def main():
    executor = ProcessPoolExecutor()
    futures = [executor.submit(task, i) for i in range(10)]
    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
    print(done.pop().result())
    executor.shutdown(wait=False, cancel_futures=True)

if __name__ == '__main__':
    main()