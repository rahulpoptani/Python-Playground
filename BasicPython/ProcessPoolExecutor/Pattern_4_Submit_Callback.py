from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

def task(name):
    sleep(random())
    return name

def custom_callback1(future):
    print(f'Callback1: {future.result()}')

def custom_callback2(future):
    print(f'Callback2: {future.result()}')

def main():
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(10)]
        for future in futures:
            future.add_done_callback(custom_callback1)
            future.add_done_callback(custom_callback1)

if __name__ == '__main__':
    main()