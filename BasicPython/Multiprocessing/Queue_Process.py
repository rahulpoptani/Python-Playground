
# Size limit Queue
# multiprocessing.Queue(maxsize=100)

# put without blocking
# queue.put(item, blocking=False, timeout=None)
# alternate
# queue.put_nowait(item)
# By default, the call to put() will block and will not use a timeout.

# with timeout blocking time
# queue.put(item, timeout=2)

#  If the queue is full, then a queue.Full exception will be raised which may be handled.
# try:
#     queue.put(item, block=False)
# except Queue.Full:
#     pass

##### Similar method options for get

# Number of items in queue:
# queue.qsize()

# Note: queue.Queue is thread-safe not Process-safe. Hence for multiprocessing use multiprocessing.Queue

# Example: Producer Consumer

from time import sleep
from random import random
from multiprocessing import Process, Queue

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
        item = queue.get()
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

