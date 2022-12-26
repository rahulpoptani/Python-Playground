# Run function as a child process

from time import sleep
from multiprocessing import Process
import multiprocessing

def task(sleep_time, message):
    sleep(sleep_time)
    print(message)

if __name__ == '__main__':
    # create a new instance of the multiprocessing.Process class and specify the function we wish to execute in a new process via the “target” argument.
    process = Process(target=task, args=(1, 'New message from another process'))
    # The start() function will return immediately and the operating system will execute the function in a separate process as soon as it is able.
    # A new instance of the Python interrupter will be created and a new thread within the new process will be created to execute our target function.
    process.start()
    print('Waiting for the process')
    process.join()

