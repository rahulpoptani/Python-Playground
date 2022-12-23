from ConsoleLogging import logging
from time import sleep
from random import random
from threading import Thread, Barrier
from queue import Queue

def producer_func(barrier, queue, identifier):
    logging.info(f'Producer {identifier}: Running')
    for i in range(10):
        value = random()
        sleep(value)
        item = (i, value)
        queue.put(item)
        logging.info(f'Producer {identifier} added {item}')
    barrier.wait()
    if identifier == 0:
        queue.put(None)
    logging.info(f'Producer {identifier}: Done')

def consumer_func(queue, identifier):
    logging.info(f'Consumer {identifier}: Running')
    while True:
        item = queue.get()
        if item is None:
            queue.put(item)
            break
        sleep(item[1])
        logging.info(f'Consumer {identifier} got: {item}')
    logging.info(f'Consumer {identifier}: Done')

queue = Queue()
n_producer = 3
barrier = Barrier(n_producer)

consumers = [Thread(target=consumer_func, args=(queue,i), name='Consumer Thread') for i in range(5)]
for consumer in consumers:
    consumer.start()

producers = [Thread(target=producer_func, args=(barrier,queue,i), name='Producer Thread') for i in range(n_producer)]
for producer in producers:
    producer.start()

for producer in producers:
    producer.join()
for consumer in consumers:
    consumer.join()