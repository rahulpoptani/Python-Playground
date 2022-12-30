# There are perhaps three main approaches to logging from multiple processes, they are:
    # 1. Use the logging module separately from each process.
    # 2. Use multiprocessing.get_logger().
    # 3. Use custom process-safe logging.

# Downside of #1 - you have to duplicate code in order to configure a separate logger for each process.
# Downside of #2 - this logger is not shared among processes and is not process-safe.

# 3. Use custom process-safe logging (recommended)
# A few approaches are described, including:
    # Use a socket handler and send messages to a logging process.
    # Use a custom handler that internally uses a shared mutex to ensure one process logs at a time.
    # Use a queue handler that uses a shared queue to send messages to a logging process.

# All approaches are similar in that they require that log messages are serialized before being stored.

from random import random
from time import sleep
from multiprocessing import current_process, Process, Queue
from logging.handlers import QueueHandler
import logging

def logger_process(queue):
    logger = logging.getLogger('app')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    while True:
        message = queue.get()
        if message is None:
            break
        logger.handle(message)

def task(queue):
    logger = logging.getLogger('app')
    logger.addHandler(QueueHandler(queue))
    logger.setLevel(logging.DEBUG)
    process = current_process()
    logger.info(f'Child {process.name} starting..')
    for i in range(5):
        logger.debug(f'Child {process.name} step {i}')
        sleep(random())
    logger.info(f'Child {process.name} done')

if __name__ == '__main__':
    queue = Queue()
    logger = logging.getLogger('app')
    logger.addHandler(QueueHandler(queue))
    logger.setLevel(logging.DEBUG)
    
    logger_p = Process(target=logger_process, args=(queue,))
    logger_p.start()

    logger.info('Main Process Started')
    processes = [Process(target=task, args=(queue,)) for _ in range(5)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    logger.info('Main process done')
    queue.put(None)

