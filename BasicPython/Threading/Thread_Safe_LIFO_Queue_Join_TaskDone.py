# LIFO Queue
# A LIFO queue or Stack is useful in many programming situations.
# 1. Undo: Maintaining changes to an object so that they can be undone or reversed in the order they were applied.
# 2. Depth-First: Maintaining a list of nodes when navigating a tree or graph in a depth-first manner.
# 3. Parsers: Maintain a list of expressions in the order they must be executed.
# 4. Backtracking: Maintain a list of options in the order they were encountered or made available, in case the current option fails.
# 5. Freshness: Maintain a list of connections or data in the reverse order they were used so the most recent can be acquired when needed

from time import sleep
from random import random
from threading import Thread
from queue import LifoQueue

# generate work
def producer_func(queue: LifoQueue):
    print('Producer Running..')
    for i in range(10):
        value = random()
        item = (i, value)
        queue.put(item)
    # Once the task is complete it will block on the queue until all items have been processed and marked as done by the consumer
    # This can be achieved by calling the join() function.
    queue.join() # Means I've pushed all the data and waiting for consumer to call task_done for all items, once the counter reaches 0 then I'll ingest None and come out
    queue.put(None)
    print('Producer Done')

def consumer_func(queue: LifoQueue):
    print('Consumer Running..')
    while True:
        item = queue.get() # it will get an item from the queue and block if there is no item yet available.
        if item is None:
            break
        # block
        sleep(item[1])
        print(f'Got: {item}')
        queue.task_done() # The item is then marked as processed via a call to task_done().
    print('Consumer Done')


queue = LifoQueue()
producer = Thread(target=producer_func, args=(queue,))
producer.start()
consumer = Thread(target=consumer_func, args=(queue,), daemon=True)
consumer.start()
# wait for threads to finish
producer.join()
consumer.join()
