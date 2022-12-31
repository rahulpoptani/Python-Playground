from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager

class CustomManager(BaseManager):
    pass

def task(number, shared_set):
    value = random()
    sleep(value)
    shared_set.add((number, value))

if __name__ == '__main__':
    CustomManager.register('set',set)
    with CustomManager() as manager:
        shared_set = manager.set()
        processes = [Process(target=task, args=(i,shared_set)) for i in range(5)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        print('Done')
        print(len(shared_set._getvalue()))
        print(shared_set)