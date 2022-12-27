
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Condition


# start a suite of processes that will wait on the condition variable to be notified before performing their processing and reporting a result. 
# The main process will block for a moment then notify all waiting processes that they can begin their work.


# The task function will acquire the condition variable and wait to be notified. Once notified it will generate a random value between 0 and 1, block for that fraction of a second then report the value.
def task(condition, number):
    print(f'Child process {number} waiting..', flush=True)
    with condition:
        condition.wait()
    value = random()
    # sleep(value)
    print(f'Process {number} got {value}')

if __name__ == '__main__':
    condition = Condition()
    processes = [Process(target=task, args=(condition, i)) for i in range(5)]
    for process in processes:
        process.start()
    sleep(3)
    with condition:
        condition.notify_all()
    for process in processes:
        process.join()
