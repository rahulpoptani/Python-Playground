# Limit the capacity of the queue.
# This can be helpful if we have a large number of producers or slow consumers. 
# It allows us to limit the number of tasks that may be in memory at any one time, 
# limiting overall memory usage of the application.

from time import sleep
from random import random
from threading import Thread
from queue import Queue

def producer_func(queue: Queue):
    print('Producer Running..')
    for i in range(10):
        value = random()
        sleep(value)
        queue.put(value)
    print('Producer Done')


def consumer_func(queue: Queue):
    print('Consumer Running..')
    while True:
        item = queue.get() # it will get an item from the queue and block if there is no item yet available.
        print(f'Got: {item}')
        queue.task_done() # The item is then marked as processed via a call to task_done().


queue = Queue(maxsize=2)

consumer = Thread(target=consumer_func, args=(queue,), daemon=True)
consumer.start()

# Run 5 producers, each ingesting 10 elements. So that the queue is alomost full most of the time
producers = [Thread(target=producer_func, args=(queue,)) for _ in range(5)]
for producer in producers:
    producer.start()
# wait for all producers to finish
for producer in producers:
    producer.join()

# wait for all work to be processed by the consumer, Means task_done has called for all the element
queue.join()
