# Most common pattern. Convert a for loop that executes a function on each item
# in a collection to use threads.

from time import sleep
from concurrent.futures import ThreadPoolExecutor

# Function with single arguments
def task1(number):
    sleep(1)
    return number

with ThreadPoolExecutor(10) as executor:
    for result in executor.map(task1, range(10)):
        print(result)

# Function with multiple arguments
def task2(value1, value2):
    sleep(1)
    return (value1, value2)

with ThreadPoolExecutor(10) as executor:
    for result in executor.map(task2, [1, 2, 3], ['a', 'b', 'c']):
        print(result)