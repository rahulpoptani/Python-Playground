# Overriding the Process class offers more flexibility than calling a target function. 
# It allows the object to have multiple functions and to have object member variables for storing state in the child process.
# It also allows functions associated with the new process to be grouped with the new object.


from time import sleep
from multiprocessing import Process

class CustomProcess(Process):
    def __init__(self, value):
        # Base class initialization is only required when CustomProcess class accept arguments. Otherwise it can be missed
        Process.__init__(self)
        self.value = value
    
    # override the run function
    def run(self):
        sleep(self.value)
        print(f'This is comming from another process: {self.value}')

if __name__ == '__main__':
    process = CustomProcess(0.5)
    process.start()
    print('Waiting for process to finish')
    process.join()
