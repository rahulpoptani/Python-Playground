from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor, as_completed

def task(name):
    sleep(random())
    return name

def main():
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(10)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    main()