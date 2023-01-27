from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor, as_completed

def task1():
    value = random()
    sleep(value)
    print(f'Task1: {value}')
    return value

def task2(value1):
    value2 = random()
    sleep(value2)
    print(f'Task2: Value1 = {value1} Value2 = {value2}')
    return value2

def main():
    with ProcessPoolExecutor(4) as executor:
        futures1 = [executor.submit(task1) for _ in range(10)]
        futures2 = list()
        for future1 in as_completed(futures1):
            result = future1.result()
            if result > 0.5:
                future2 = executor.submit(task2, result)
                futures2.append(future2)

if __name__ == '__main__':
    main()