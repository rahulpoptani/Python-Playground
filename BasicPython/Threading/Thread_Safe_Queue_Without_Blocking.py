# This might be useful if we wish to use busy waiting in the consumer task 
# to check other states or perform other tasks while waiting for data to arrive on the queue

from time import sleep
from random import random
from threading import Thread
from queue import Queue, Empty

# generate work
def producer_func(queue: Queue):
    print('Producer Running..')
    for i in range(10):
        value = random()
        # block for a while
        sleep(value)
        # add to queue
        queue.put(value)
    # all done - add None to signal that work is done
    queue.put(None)
    print('Producer Done')

# consume work
def consumer_func(queue: Queue):
    print('Consumer Running..')
    while True:
        try:
            item = queue.get(block=False)
        except Empty:
            print('Consumer got nothing, waiting for a while')
            sleep(0.5)
            continue
        if item is None:
            break
        print(f'Got: {item}')
    # all done
    print('Consumer Done')

queue = Queue()
consumer = Thread(target=consumer_func, args=(queue,))
consumer.start()
producer = Thread(target=producer_func, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()