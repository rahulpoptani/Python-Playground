# When sharing data between the queue, need to implement two different method
# Ex: Two method for two threads

from queue import Queue
from random import randint
import threading
import time

queue = Queue()

def push_in(queue: Queue):
    for _ in range(10):
        time.sleep(1)
        data = randint(1,99)
        print(f'In Queue: {data}')
        queue.put(data)

def pull_out(queue: Queue):
    for _ in range(10):
        time.sleep(1.5)
        data = queue.get()
        print(f'Out Queue: {data}')


thread1 = threading.Thread(target=push_in, args=(queue,))
thread2 = threading.Thread(target=pull_out, args=(queue,))

thread1.start()
thread2.start()