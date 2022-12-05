# A custome thread must override the run() function in order to specify the code that will run in a new thread

import threading
import time

# Given that it is custom class, you can define constructor for the class and use it to pass in data that may be needed to the run() function
# You can also define additional functions on the class to split up the work you may need to complete in another thread
# Finally attributes can also be used to store the resuls of any calculations or IO performed in another thread

# custom thread class
class CustomThread(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        for _ in range(3):
            time.sleep(1)
            print(f'From task {self.value} slept: {_}')
        # assume computation returned some output
        self.output = 10

# create the thread
thread = CustomThread('argument')

# start the thread
thread.start()
print('This will run immediately')

# waiting for the thread to finish
thread.join()
print('This will print when thread is finished execution')

# retrive the output when the thread finishes
print(f'Output from thread: {thread.output}')