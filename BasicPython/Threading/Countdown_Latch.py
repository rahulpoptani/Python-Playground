# we may need to coordinate one or more threads based on the work completed by many other threads.
# For example:
    # Waiting for multiple parts of a solution to be complete before piecing them together.
    # Waiting for all subtasks to complete before moving on to the next task.
# Solving this type of coordination problem requires keeping track of the number of elements 
# or subtasks that have completed in a thread-safe manner, and not moving on until all elements have completed

# A latch can be used to address this type of problem as it provides a thread-safe counter and notification mechanism once the counter reaches zero.

# It is created in the closed position and requires a count to be decremented until zero before opening.
# The count is decremented by threads that pass through the latch, calling a count_down() function. 
# This is a non-blocking call, allowing the caller to proceed immediately.
# Other threads register interest in the latch by calling wait() to block on the latch until it is opened.

# A latch is a one-use structure and is not reset after use. Once open, 
# additional threads that may wait on the latch will not block but will instead return immediately.

# Internally, the latch may count up or count down, but typically decrements with each arrival, hence the common name “countdown latch“. 

# Latch Vs Barrier:
    # A latch can have any number of waiting threads and a fixed number of expected arrivals before opening.
    # A barrier has a fixed number of waiting threads that are all waiting for each other to arrive before opening.
    # Latch allows threads that arrive to carry on and to have any number of other waiting threads. 
    # Whereas the barrier requires that each thread that arrives must also wait for all other threads to arrive.

# Implementation of Latch

from threading import Condition, Thread
from time import sleep
from random import random

class CountDownLatch():
    # The constructor will take a count specified by the user, indicating the expected number of parties to arrive before the latch is opened.
    def __init__(self, count):
        self.count = count
        self.condition = Condition()
    # The count_down() function must first acquire the condition before doing anything to ensure any checking and changing of the internal count is thread safe.
    def count_down(self):
        with self.condition:
            # we need to check if the latch is already open, and if so return immediately.
            if self.count == 0:
                return
            # decrement the counter
            self.count -= 1
            # we can check if the counter has reached zero and whether we should notify all waiting threads.
            if self.count == 0:
                self.condition.notify_all()
    
    def wait(self):
        with self.condition:
        # We can then check if the latch is already open, in which case we can return immediately.
            if self.count == 0:
                return
            # Otherwise, we can wait on the condition to be notified that the latch will be opened.
            self.condition.wait()
    # extra functios can be added like, getCount, resetCount if only latch is open, etc.

# Example:
# we will start a number of threads, each of which must perform some task then trigger the latch to signal they are done. 
# The coordinating thread will wait for all threads to complete their work before carrying on.

def task(latch, i):
    sleep(random()*10)
    latch.count_down()
    print(f'Thread {i} done.')

latch = CountDownLatch(5)

for i in range(5):
    thread = Thread(target=task, args=(latch, i))
    thread.start()

print('Main waiting for the latch..')
latch.wait()
print('Main done')

