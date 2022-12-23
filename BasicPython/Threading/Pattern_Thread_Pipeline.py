# A pipeline of tasks executed by threads can be a useful pattern in concurrent programming.

# For example, we might imagine a series of steps to search a series of webpages for a keyword.
# The first step may read a list of URLs from a file and produce each URL as a task. The next step may be responsible for downloading the URL into memory. The next step may be responsible for saving the downloaded content to file. The next step may be responsible for parsing the HTML from the downloaded file and the final step may be responsible for searching the text content for a keyword.
# For example:
    # Step 1: Load a file of URLs and produce each URL as a task.
    # Step 2: Download a URL from the internet into memory.
    # Step 3: Save content from memory to file.
    # Step 4: Read a file and parse the HTML.
    # Step 5: Search text content of document for keyword.
    # Step 6: Collate and report results.

# The decomposition of the application into a pipeline offers a number of benefits, for example:
    # Clear definition of subtasks with specific inputs and outputs, e.g. better design
    # Concurrency execution of subtasks, e.g. faster overall execution time.
    # Configurable concurrency of subtasks, e.g. some tasks will benefit more than others.
    # Responsive application, e.g. results may start appearing sooner than processing each step in a batch.



from random import random
from time import sleep
from threading import Thread
from queue import Queue
import logging
import sys

def task1(queue_out):
    logging.info('Started')
    for i in range(10):
        value = random()
        sleep(value)
        item = [i, value]
        queue_out.put(item)
        logging.info(f'Generated {item}')
    queue_out.put(None)
    logging.info('Done')

def task2(queue_in, queue_out):
    logging.info('Started')
    while True:
        item = queue_in.get()
        if item is None:
            queue_out.put(item)
            break
        value = random()
        sleep(value)
        new_item = item + [value]
        queue_out.put(new_item)
        logging.info(f'Got {item} Generated {new_item}')
    logging.info('Done')

def task3(queue_in):
    logging.info('Started')
    while True:
        item = queue_in.get()
        if item is None:
            break
        logging.info(f'Got {item}')
    logging.info('Done')

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('[%(levelname)s] [%(threadName)s] %(message)s'))
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

queue1 = Queue()
thread1 = Thread(target=task1, args=(queue1,), name='Task1')
thread1.start()

queue2 = Queue()
thread2 = Thread(target=task2, args=(queue1, queue2), name='Task2')
thread2.start()

thread3 = Thread(target=task3, args=(queue2,), name='Task3')
thread3.start()

thread1.join()
thread2.join()
thread3.join()
