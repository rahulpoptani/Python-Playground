# You can use a manager to create a namespace that may be used to share primitive variables safely with processes.
# Primitive variables can be added to the namespace directly by defining them.
# Any arbitrary variable names may be used, except those that start with an underscore as they will become members on the proxy object itself instead of the hosted namespace.

# Although reading and writing values is process-safe, some operations are not.
# it is NOT process-safe to add or subtract values from primitives on the namespace. This is because modifying a value is not atomic, instead it is a three step process of read, compute, and write.
# As such, modification operations like adding, subtracting and incrementing values are not process safe and should be avoided.


from time import sleep
from random import random
from multiprocessing import Process, Manager

def task1(shared_namespace):
    value = random()
    sleep(value)
    shared_namespace.task1 = value
    print(f'Task1 sees {shared_namespace.main} got {value}', flush=True)

def task2(shared_namespace):
    value = random()
    sleep(value)
    shared_namespace.task2 = value
    print(f'Task2 sees {shared_namespace.task1} got {value}', flush=True)

if __name__ == '__main__':
    with Manager() as manager:
        namespace = manager.Namespace()
        namespace.main = 55
        process = Process(target=task1, args=(namespace,))
        process.start()
        process.join()
        process = Process(target=task2, args=(namespace,))
        process.start()
        process.join()
        print(f'Main sees: {namespace}')