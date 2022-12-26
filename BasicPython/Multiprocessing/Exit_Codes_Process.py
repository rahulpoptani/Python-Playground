# You can set an exit code for a process via sys.exit() and retrieve the exit code via the exitcode attribute on the multiprocessing.Process class.
# An exit code or exit status is a way for one process to share with another whether it is finished and if so whether it finished successfully or not
# if the process exits normally, the exit code will be set to zero. If the process terminated with an error or exception, the exit code will be set to one.
# A process can also set its exit code when explicitly exiting.
# This can be achieved by calling the sys.exit() function and passing the exit code as an argument.

    # 0, None: Success
    # 1: Error
    # 2: Command line syntax errors
    # 120: Error during process cleanup.
    # 255: Exit code out of range.

from time import sleep
from multiprocessing import Process
import sys 

def task():
    sleep(1)
    sys.exit(0)
    # sys.exit('Bad Error') # will return sys.exit(1) along with message
    # raise Exception('Bad Error') # will return sys.exit(1) along with message

if __name__ == '__main__':
    child = Process(target=task)
    child.start()
    print(f'Child exit code: {child.exitcode}') # None, as the process is not completed
    child.join()
    print(f'Child exit code: {child.exitcode}')