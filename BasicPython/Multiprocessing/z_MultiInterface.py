# Simple Interface with 1 method.
# Implemenet interface in two classes and override 1 method with print statement
# Output: Both should only consider objects from there classes and print it's respective methods
# Parallel Execution using Dask

import abc
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from dask.distributed import Client
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(food: str) -> None:
        pass

class Dog(Animal):
    def eat(self, food: str) -> None:
        time.sleep(1)
        return (f'Dog eating: {food}')
class Cat(Animal):
    def eat(self, food: str) -> None:
        time.sleep(1)
        return (f'Cat eating: {food}')

dog = Dog()
cat = Cat()

start = time.perf_counter()

if __name__ == '__main__':
    t = ThreadPoolExecutor(4)
    p = ProcessPoolExecutor()

    # Thread Pool - Run any 1 to compare performance
    futures = []
    futures.append(t.submit(dog.eat, 'DogFood'))
    futures.append(t.submit(cat.eat, 'CatFood'))
    results = [future.result() for future in futures]
    print(results)

    # ProcessPool - Run any 1 to compare performance
    # futures = []
    # futures.append(p.submit(dog.eat, 'DogFood'))
    # futures.append(p.submit(cat.eat, 'CatFood'))
    # results = [future.result() for future in futures]
    # print(results)

    # Using Dask - Run any 1 to compare performance - Takes too much time then above method. TODO
    # client = Client()
    # futures = []
    # futures.append(client.submit(dog.eat, 'DogFood'))
    # futures.append(client.submit(cat.eat, 'CatFood'))
    # results = [future.result() for future in futures]
    # print(results)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')

    

# dog.eat('DogFood')
# cat.eat('CatFood')

