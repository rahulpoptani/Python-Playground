# We may need to start new threads in child process
# Ex: When we need to perform many IO bound tasks within each child process

from random import random
from time import sleep
from threading import Thread, current_thread
from multiprocessing import Process, current_process

def thread_task():
    sleep(3*random())
    process_name = current_process().name
    thread_name = current_thread().name
    print(f'Thread {thread_name} in process: {process_name} done', flush=True)

def process_task():
    threads = [Thread(target=thread_task) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    process_name = current_process().name
    print(f'Process {process_name} done', flush=True)

if __name__ == '__main__':
    processes = [Process(target=process_task) for _ in range(5)]
    for child in processes:
        child.start() 
    for child in processes:
        child.join()
    process_name = current_process().name
    print(f'Main process: {process_name} done', flush=True)
