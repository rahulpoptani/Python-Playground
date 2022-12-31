
from time import sleep
from multiprocessing import Process, parent_process
import os

def is_orphan():
    parent = parent_process()
    if parent is None or not parent.is_alive():
        return True
    return False

def task():
    print(f'Orphaned: {is_orphan()}', flush=True)
    sleep(3)
    print(f'Orphaned: {is_orphan()}', flush=True)
    print(f'Parent Alive?: {parent_process().is_alive()}', flush=True)

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    sleep(1)
    print('Main all done')
    os._exit(0)
