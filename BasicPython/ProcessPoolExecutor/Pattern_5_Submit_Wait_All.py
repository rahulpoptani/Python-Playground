from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor, wait

def task(name):
    sleep(random())
    print(name)

def main():
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(10)]
        wait(futures)
    print('All Done')

if __name__ == '__main__':
    main()