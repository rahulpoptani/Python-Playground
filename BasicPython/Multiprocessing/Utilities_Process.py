# There are a number of utilities we can use when working with processes within a Python process.

from time import sleep
from multiprocessing import active_children
from multiprocessing import Process
from multiprocessing import cpu_count
from multiprocessing import current_process

def task():
    sleep(1)
    print(f'Child Current Process: {current_process()}')

if __name__ == '__main__':
    
    # get CPU Count:
    print(f'Total CPU Count: {cpu_count()}')

    # get current process details
    print(f'Parent: Current Process: {current_process()}')
    
    # Spawn 5 process, active childs
    processes = [Process(target=task) for _ in range(5)]
    for process in processes:
        process.start()
    
    # get the list of all active child process
    children = active_children()
    print(f'Active Children: {len(children)}')
    for child in children:
        print(child)
    

