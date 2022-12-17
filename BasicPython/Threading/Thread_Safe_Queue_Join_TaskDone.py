# Another approach after "Without Blocking" and "Timeout"
# An alternative approach is to have threads wait on the queue directly and to have the consumer thread mark tasks as done.
# This can be achieved via the join() and task_done() functions on the queue.Queue.
# The producer thread can be updated to no longer send a None value into the queue to indicate no further tasks.

from time import sleep
from random import random
from threading import Thread
from queue import Queue

# generate work
def producer_func(queue: Queue):
    print('Producer Running..')
    for i in range(10):
        value = random()
        # block for a while
        sleep(value)
        # add to queue
        queue.put(value)
    # all done - add None to signal that work is done
    print('Producer Done')

# consume work
# The consumer thread will no longer check for None messages, 
# and to mark each task as completed via a call to task_done().
def consumer_func(queue: Queue):
    print('Consumer Running..')
    while True:
        item = queue.get() # it will get an item from the queue and block if there is no item yet available.
        print(f'Got: {item}')
        queue.task_done() # The item is then marked as processed via a call to task_done().

# The producer thread will run until there are no longer any tasks to add to the queue and will terminate. The consumer thread will now run forever.
# To achieve this, we can mark the consumer thread as a background daemon thread by setting the “daemon” argument to True when configuring it.
# The Python process will exit once all non-daemon threads have terminated, including the producer thread and the main thread, but not the consumer thread.
queue = Queue()
consumer = Thread(target=consumer_func, args=(queue,), daemon=True)
consumer.start()
producer = Thread(target=producer_func, args=(queue,))
producer.start()

# the main thread no longer needs to wait on the producer and consumer threads to terminate before terminating itself.
# Instead, it can wait on the queue itself and stop waiting once the consumer has processed all tasks.
# This may result in a race condition, as it is possible for no items to be added to the queue before the main thread reaches this line, in which case the main thread will terminate immediately.
# Therefore, we can have the main thread first wait on the producer thread to complete, in which case we know all work has been added to the queue, and then wait on the queue itself for that work to be processed.

producer.join()
queue.join()
