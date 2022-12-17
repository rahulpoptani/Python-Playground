# create a producer thread that will generate ten random numbers and put them on the queue.
# create a consumer thread that will get numbers from the queue and report their values.

# The queue.Queue provides a way to allow these producer and consumer threads to communicate data with each other.

from time import sleep
from random import random
from threading import Thread
from queue import Queue

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
        item = queue.get() # it will get an item from the queue and block if there is no item yet available.
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