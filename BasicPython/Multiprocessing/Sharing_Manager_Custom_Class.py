# We can use a manager to create and manage a centralized version of a custom class.
# This requires a few steps:
    # 1. Defining a custom class.
        # The class should be serializable, e.g. picklable.
        # If we expect the class to be accessed and modified from multiple processes concurrently, then it is a good idea to protect any internal state using a mutex lock.
    # 2. Defining a custom Manager class that extends BaseManager.
    # 3. Registering the custom class with the custom manager.
    # 4. Creating an instance of the custom manager.
    # 5. Creating an instance of the custom class from the manager instance.


from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager

class MyCustomClass():
    def __init__(self, data):
        self.data = data
        self.storage = list()
    def task(self):
        value = random()
        sleep(value)
        self.data = self.data + value
        self.storage.append((self.data, value))
        return self.data
    def get_storage(self):
        return self.storage

class CustomManager(BaseManager):
    pass

def work(shared_custom):
    value = shared_custom.task()
    print(f'Child Got: {value}')

if __name__ == '__main__':
    CustomManager.register('MyCustomClass', MyCustomClass)
    with CustomManager() as manager:
        shared_custom = manager.MyCustomClass(10)
        value = shared_custom.task()
        print(f'Main Got: {value}')
        processes = [Process(target=work, args=(shared_custom,)) for i in range(4)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        print('Done')
        for t in shared_custom.get_storage():
            print(t)