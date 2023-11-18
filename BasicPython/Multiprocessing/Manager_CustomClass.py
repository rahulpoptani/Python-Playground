from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager
 
# Step1: Define a custom class
class MyCustomClass:
    def __init__(self, data):
        self.data = data
        self.storage = list()
 
    def task(self):
        value = random()
        sleep(value)
        new_value = self.data * value
        self.storage.append((self.data, value, new_value))
        return new_value
 
    def get_storage(self):
        return self.storage
 
# Step2: Define a custom manager in order to use the manager to create and manage custom classes.
# The custom class does not need to override the constructor or any methods, nor define any functionality.
class CustomManager(BaseManager):
    pass
 
# Custom function to be executed in a child process
def work(shared_custom):
    # call the function on the shared custom instance
    value = shared_custom.task()
    print(f'>child got {value}')
 
if __name__ == '__main__':
    # Step3: Register the custom class with CustomManager
    CustomManager.register('MyCustomClass', MyCustomClass)
    
    with CustomManager() as manager:
        # Step4: create an instance of our custom class using the manager.
        shared_custom = manager.MyCustomClass(10)
        # call the function on the shared custom instance
        value = shared_custom.task()
        # report the value
        print(f'>main got {value}')
        # start some child processes
        processes = [Process(target=work, args=(shared_custom,)) for i in range(4)]
        # start processes
        for process in processes:
            process.start()
        # wait for processes to finish
        for process in processes:
            process.join()
        # all done
        print('Done')
        # report all values stored in the central object
        for t in shared_custom.get_storage():
            print(t)