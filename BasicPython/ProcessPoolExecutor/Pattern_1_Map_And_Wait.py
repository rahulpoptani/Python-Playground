from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# Single Argumtn
def task1(name):
    sleep(random())
    return name

def main1():
    with ProcessPoolExecutor() as executor:
        for result in executor.map(task1, range(10)):
            print(result)

if __name__ == '__main__':
    main1()

# Pass Multiple Argument
def task2(value1, value2):
    sleep(random())
    return (value1, value2)

def main2():
    with ProcessPoolExecutor() as executor:
        for result in executor.map(task2, [1,2,3],[4,5,6]):
            print(result)

if __name__ == '__main__':
    main2()
