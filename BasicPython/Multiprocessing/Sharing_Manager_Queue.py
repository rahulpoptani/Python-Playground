from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Manager

def task(number, shared_queue):
    value = random()
    sleep(value)
    shared_queue.put((number, value))

if __name__ == '__main__':
    with Manager() as manager:
        shared_queue = manager.Queue()
        n_task = 50
        processes = [Process(target=task, args=(i,shared_queue)) for i in range(n_task)]
        for process in processes:
            process.start()
        for _ in range(n_task):
            item = shared_queue.get()
            print(f'Got {item}')
