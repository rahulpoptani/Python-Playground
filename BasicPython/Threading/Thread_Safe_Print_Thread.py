# When printing aquire mutex lock

from random import random
from time import sleep
from threading import Thread
from queue import Queue

def printer(queue):
    while True:
        message = queue.get()
        print(message)

def task(number, queue):
    value = random()
    sleep(value)
    queue.put(f'Thread {number} got value: {value}')

queue = Queue()
printer_thread = Thread(target=printer, args=(queue,), daemon=True, name='Printer')
printer_thread.start()

threads = [Thread(target=task, args=(i, queue)) for i in range(1000)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

