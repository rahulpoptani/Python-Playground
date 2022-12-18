# File writing by multiple thread is NOT thread safe
# There are two approches to make it thread safe
# 1. Acquire Lock when writing
# 2. Have a dedicated thread for writing file and share information using Queue

from random import random
from threading import Thread
from queue import Queue

def file_writer(filepath, queue):
    with open(filepath, 'w') as file:
        while True:
            line = queue.get()
            if line is None:
                break
            file.write(line)
            file.flush()
            queue.task_done()
        queue.task_done()

def task(number, queue):
    for i in range(1000):
        value = random()
        queue.put(f'Thread {number} got {value} \n')

queue = Queue()
filepath = 'output.txt'

writer_thread = Thread(target=file_writer, args=(filepath, queue), daemon=True)
writer_thread.start()

threads = [ Thread(target=task, args=(i, queue)) for i in range(1000)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
queue.put(None)
queue.join()