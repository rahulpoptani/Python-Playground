# An event is a process-safe boolean flag.
# An event is a simple concurrency primitive that allows communication between processes.
# The multiprocessing.Event provides an easy way to share a boolean variable between processes that can act as a trigger for an action.

# event.is_set() # check if event is set
# event.set() # set a event
# event.clear() # marked event as not set
# event.wait() # calling wait will block until event is set
# event.wait(timeout=5) # calling wait with timeout will block only for configured timeout

from time import sleep
from random import random
from multiprocessing import Process, Event

def task(event, number):
    print(f'Process {number} waiting..', flush=True)
    event.wait()
    print(f'Process {number} finished', flush=True)

if __name__ == '__main__':
    event = Event()
    processes = [Process(target=task, args=(event, i)) for i in range(5)]
    for process in processes:
        process.start()
    print('Main process blocking for some work..')
    sleep(2)
    print('Work Done: Notifying all processes..')
    event.set()
    for process in processes:
        process.join()