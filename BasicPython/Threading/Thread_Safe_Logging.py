# We can log directly from multiple threads because the logging module is thread-safe.
# This may be for many reasons, such as:
    # Different threads may perform different tasks and may encounter a range of events.
    # Worker threads may encounter exceptions that need to be stored, but should not halt the program.
    # Background tasks may need to report progress over the duration of the program

# Internally, the logging module uses mutual exclusion (mutex) locks to ensure that logging handlers are protected from race conditions from multiple threads.


from random import random
from time import sleep
from threading import Thread
import logging

def task(number, threshold):
    logging.info(f'Thread {number} starting..')
    for i in range(5):
        value = random()
        sleep(value)
        if value < threshold:
            logging.warning(f'Thread {number} value less than {threshold}, stopping..')
            break
        logging.info(f'Thread {number} completed successfully')

# For console logging
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('[%(levelname)s] %(name)s: [%(threadName)s] %(message)s'))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
# For file logging 
# handler = logging.FileHandler('application.log')
# handler.setLevel(logging.DEBUG)
# handler.setFormatter(logging.Formatter('[%(levelname)s] %(name)s: [%(threadName)s] %(message)s'))
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(handler)

threads = [Thread(target=task, args=(i, 0.1)) for i in range(5)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()