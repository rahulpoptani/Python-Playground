
from time import sleep
from random import random
from multiprocessing import Process, Queue
from queue import Empty

def producer(queue):
    print('Producer: Running', flush=True)
    for i in range(10):
        value = random()
        sleep(value)
        queue.put(value)
    queue.put(None)
    print('Producer: Done', flush=True)

def consumer(queue):
    print('Consumer: Running', flush=True)
    while True:
        try:
            item = queue.get(timeout=0.5)
        except Empty:
            print('Consumer: Got Nothing, gave up waiting..', flush=True)
            continue
        if item is None:
            break
        print(f'Got: {item}', flush=True)
    print('Consumer: Done')

if __name__ == '__main__':
    queue = Queue()
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    producer_process.join()
    consumer_process.join()

