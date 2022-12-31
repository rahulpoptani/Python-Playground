from time import sleep
from multiprocessing import Process
import sys

def task():
    print('Child process running')
    sleep(2)
    print('Exiting..')
    sys.exit(1)
    print('This wont run')

if __name__ == '__main__':
    child = Process(target=task)
    child.start()
    child.join()
    print(f'Alive: {child.is_alive()}')
    print(f'Exitcode: {child.exitcode}')
