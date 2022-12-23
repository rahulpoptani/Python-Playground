from ConsoleLogging import logging
from time import sleep
from random import random
from threading import Thread
from queue import Queue

def producer_func(queue):
    logging.info('Producer: Running')
    for i in range(10):
        value = random()
        sleep(value)
        item = (i, value)
        queue.put(item)
        logging.info(f'Producer added {item}')
    queue.put(None)
    logging.info('Producer: Done')

def consumer_func(queue):
    logging.info('Consumer: Running')
    while True:
        item = queue.get()
        if item is None:
            break
        sleep(item[1])
        logging.info(f'Consumer got: {item}')
    logging.info('Consumer: Done')

queue = Queue()
consumer = Thread(target=consumer_func, args=(queue,), name='Consumer Thread')
consumer.start()
producer = Thread(target=producer_func, args=(queue,), name='Producer Thread')
producer.start()
producer.join()
consumer.join()