from time import sleep
from os import getpid, getppid
from threading import current_thread
from concurrent.futures import ProcessPoolExecutor

def custom_callback(future):
    print(f'Callback pid={getpid()}, ppid={getppid()}, thread={current_thread().name}')

def work():
    sleep(0.1)
    print(f'Worker pid={getpid()}, ppid={getppid()}, thread={current_thread().name}')

if __name__ == '__main__':
    print(f'Main pid={getpid()}, ppid={getppid()}, thread={current_thread().name}')
    with ProcessPoolExecutor(2) as executor:
        future = executor.submit(work)
        future.add_done_callback(custom_callback)

# Note: Callbacks are run using Thread and not separate process
# The main thread will create a new thread and run the callback