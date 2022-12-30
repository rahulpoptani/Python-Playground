# A problem when using queues is knowing when all items in the queue have been processed by consumer processes.

# Why care when all tasks are done?
# For example:
    # A producer process may want to wait until all work is done before adding new work.
    # A producer process may want to wait for all tasks to be done before sending a shutdown signal.
    # A main process may want to wait for all tasks to be done before terminating the program.

# The multiprocessing.JoinableQueue class offers two additional methods for joining a queue and marking items on the queue as done.

# When a consumer process calls get() to retrieve the item from the queue, it may need to do additional work to it before the task is considered complete.
# Once complete, the process may then call the task_done() method on the queue to indicate that the item that was just retrieved has been completely processed.

# This is helpful to other processes that may be interested to know once all tasks that have been added to the queue have been completed.
# Other processes can wait for all tasks currently on the queue to be completed by calling the join() function

# The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer calls task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, join() unblocks.

# If the task_done() function is called more times than there are items on the queue, then a ValueError will be raised to indicate the invalid state.


from time import sleep
from random import random
from multiprocessing import Process, JoinableQueue

def producer(queue):
    print('producer Starting', flush=True)
    for i in range(10):
        task = (i, random())
        print(f'Producer added {task}', flush=True)
        queue.put(task)
    queue.put(None)
    print('Producer Finished', flush=True)

def consumer(queue):
    print('Consumer Staring', flush=True)
    while True:
        task = queue.get()
        if task is None:
            break
        sleep(task[1])
        print(f'Consumer got: {task}', flush=True)
        queue.task_done()
    queue.task_done() # for the None message
    print('Consumer Finished', flush=True)

if __name__ == '__main__':
    queue = JoinableQueue()
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    producer_process.join()
    print('Main found that producer is finsihed', flush=True)
    queue.join()
    print('Main found that all tasks are processed', flush=True)



