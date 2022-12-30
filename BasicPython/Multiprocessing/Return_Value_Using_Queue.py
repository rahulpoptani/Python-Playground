from random import random
from time import sleep
from multiprocessing import Process, Queue

def task(queue):
    data = random()
    print(f'Generated {data}', flush=True)
    sleep(data)
    queue.put(data)

if __name__ == '__main__':
    queue = Queue()
    process = Process(target=task, args=(queue,))
    process.start()
    value = queue.get()
    print(f'Returned {value}')
