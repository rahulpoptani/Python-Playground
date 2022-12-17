# How can we know when all items have been processed in a queue?

# Why Care When All Tasks Are Done?
# Example:
    # A producer thread may want to wait until all work is done before adding new work.
    # A producer thread may want to wait for all tasks to be done before sending a shutdown signal.
    # A main thread may want to wait for all tasks to be done before terminating the program.
# The condition of all tasks being processed is not only the case that all items put on the queue have been retrieved, but have been processed by the thread that retrieved them.

# How to Know When All Tasks Are Done?
# A thread can block and be notified when all current items or tasks on the queue are done by calling the Queue.join() function.
# Block means that the calling thread will wait until the condition is met, specifically that all tasks are done. The Queue.join() function will not return until then.
# Notified means that the blocked thread will be woken up and allowed to proceed when all tasks are done. This means that the join() function will return at this time allowing the thread to continue on with the next instructions.

# Multiple different threads may join the queue and await the state that all tasks are marked done.
# If there are no tasks in the queue, e.g. the queue is empty, then the join() function will return immediately.

# Note: The Queue.join() function only works if threads retrieving items or tasks from the queue via Queue.get() also call the Queue.task_done() function.
# The Queue.task_done() function is called by the consumer thread (e.g. the thread that calls Queue.get()) only after the thread has finished processing the task retrieved from the queue.

# If there are multiple consumer threads, then for join() to function correctly, each consumer thread must mark tasks as done.

# If processing the task may fail with an unexpected Error or Exception, it is a good practice to wrap the processing of the task in a try-finally pattern.

# IMPORTANT: USE THIS APPROACH. TRY [EXCEPT] FINALLY
# item = queue.get()
# try:
#     # process
# finally:
#     queue.task_done()

# This ensures that the task is marked done in the queue, even if processing the task fails.
# Note: Too many calls to task_done will raise ValueError

# Explanation and Example

from time import sleep
from random import random
from queue import Queue
from threading import Thread

def producer_func(queue: Queue):
    print('Producer Starting')
    for i in range(10):
        task = (i, random())
        print(f'Producer added {task}')
        queue.put(task)
    # the producer will put the value None on the queue to signal to the consumer that there are no further tasks.
    # This is called a Sentinel Value and is a common way for threads to communicate via queues to signal an important event, like a shutdown.
    queue.put(None)
    print('Producer Finished')

def consumer_func(queue: Queue):
    print('Consumer Starting')
    while True:
        #  it will get an item from the queue and block if there is no item yet available.
        task = queue.get()
        # If the item retrieved from the queue is the value None, then the task will break the loop and terminate the thread.
        if task is None:
            break
        sleep(task[1])
        print(f'Consumer got {task}')
        # the item is then marked as processed via a call to task_done().
        queue.task_done()
    # Finally, just prior to the thread exiting, it will mark the signal to terminate as processed.
    # This is for the None signal
    queue.task_done()
    print('Consumer Finished')

queue = Queue()
# we can configure and start the producer thread, which will generate tasks and add them to the queue for the consumer to retrieve.
producer = Thread(target=producer_func, args=(queue,))
producer.start()

# configure and start the consumer thread, which will patiently wait for work to arrive on the queue.
consumer = Thread(target=consumer_func, args=(queue,))
consumer.start()

# The main thread will then block until the producer thread has added all work to the queue and the thread has terminated.
producer.join()
print('Main found that the producer has finished')

# The main thread will then block on the queue with a call to join() until the consumer has retrieved all values from the queue and processed them appropriately. This includes the final signal that there are no further task items to process.
queue.join()
print('Main found that all task are processed')

# It is important that the main thread blocks on the producer thread first, before blocking on the queue. This is to avoid a possible race condition.
# For example, if the main thread blocked on the queue directly, it is possible that at that time for the queue to be empty, in which case the call would return immediately. Alternatively, it may join at a time when there are only a few tasks on the queue, they are consumed by the consumer thread and the join call returns.
# The problem is that in both of these cases, we don’t know if the call to join returned because all tasks were marked done or just a subset of tasks that had been added to the queue at the time join was called.
# By waiting for the producer thread to terminate first, we know that all tasks that could be added to the queue have been added to the queue. By blocking on the queue after the producer has finished, we know that when the call to join returns, that all tasks were added to the queue, all tasks were retrieved from the queue and all retrieved tasks were marked as done.

# queue.qsize and queue.empty cannot be used, because it will return value at the time of calling. There could be case where some data pushed by producer is consumer bu consumer and qsize will result 0, but producer has still more to produce.

# Is Queue.join() related to Thread.join()?
# No.
# Calling join() on a queue will block and return once the number of calls to task_done() matches the number of calls to put() at the time that join() is called.
# Calling join() a thread will block until the target thread terminates.

# Do All Consumer Threads Need To Call task_done()?
# Yes.
# If a thread is blocked by calling join() on the queue, then all threads that are retrieving items from the queue via get() must call task_done() in order for the blocked thread to be notified correctly.



