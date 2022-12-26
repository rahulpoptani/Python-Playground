# The main process is the parent process that executes your program.

# There are a number of ways that the main process can be identified.
# They are:
    # The main process has a distinct name of “MainProcess“.
    # The main process does not have a parent process.
    # The main process is an instance of the multiprocessing.process._MainProcess class.

from multiprocessing import current_process
from multiprocessing import parent_process
from multiprocessing import Process


def child2():
    # Get child process details
    process = parent_process()
    print(f'From Grand Child: My Parent: {process} PID: {process.pid}')
    current = current_process()
    print(f'From Grand Child: Me: {current} PID: {current.pid}')

def child1():
    # Get child process details
    process = parent_process()
    print(f'From Child: My Parent: {process} PID: {process.pid}')
    current = current_process()
    print(f'From Child: Me: {current} PID: {current.pid}')
    Process(target=child2).start()


if __name__ == '__main__':
    process = Process(target=child1)
    process.start()
    # Get main process details
    main_process = current_process()
    print(f'From Main: {main_process} PID: {main_process.pid}')
    main_parent = parent_process()
    print(f'From Main: My Parent: {main_parent} ')
    process.join()

# Ways to identify MainProcess?
def is_main_process():
    return current_process().name == 'MainProcess'

def is_main_process():
    return parent_process() == None

def is_main_process():
    return not issubclass(type(current_process), Process)

