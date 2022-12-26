# Instance variable attributes can be shared between processes via the multiprocessing.Value and multiprocessing.Array classes.
# These classes explicitly define data attributes designed to be shared between processes in a process-safe manner.
# Shared variables mean that changes made in one process are always propagated and made available to other processes.

from time import sleep
from multiprocessing import Process, Value

class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
        # The constructor of the multiprocessing.Value class requires that we specify the data type and an initial value.
        self.data = Value('i', 0)
    def run(self):
        sleep(1)
        self.data.value = 99
        print(f'Child Stored: {self.data.value}')

if __name__ == '__main__':
    process = CustomProcess()
    process.start()
    print('Waiting for child process to finish')
    process.join()
    print(f'Parent got: {process.data.value}')
