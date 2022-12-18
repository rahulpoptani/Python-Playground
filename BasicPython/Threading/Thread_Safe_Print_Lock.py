# When printing aquire mutex lock

from random import random
from time import sleep
from threading import Thread, Lock

def task(number, lock):
    value = random()
    sleep(value)
    with lock:
        print(f'Thread {number} got value: {value}')

lock = Lock()
threads = [Thread(target=task, args=(i, lock)) for i in range(1000)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

