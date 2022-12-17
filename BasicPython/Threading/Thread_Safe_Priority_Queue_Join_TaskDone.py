# LIFO Queue
# A LIFO queue or Stack is useful in many programming situations.
# 1. Undo: Maintaining changes to an object so that they can be undone or reversed in the order they were applied.
# 2. Depth-First: Maintaining a list of nodes when navigating a tree or graph in a depth-first manner.
# 3. Parsers: Maintain a list of expressions in the order they must be executed.
# 4. Backtracking: Maintain a list of options in the order they were encountered or made available, in case the current option fails.
# 5. Freshness: Maintain a list of connections or data in the reverse order they were used so the most recent can be acquired when needed

from time import sleep
from random import random, randint
from threading import Thread
from queue import PriorityQueue

# generate work
def producer_func(queue: PriorityQueue):
    print('Producer Running..')
    for i in range(10):
        value = random()
        priority = randint(0,10)
        item = (priority, value)
        queue.put(item)
    queue.join()
    queue.put(None)
    print('Producer Done')

def consumer_func(queue: PriorityQueue):
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


queue = PriorityQueue()

producer = Thread(target=producer_func, args=(queue,))
producer.start()

consumer = Thread(target=consumer_func, args=(queue,), daemon=True)
consumer.start()
# wait for threads to finish
producer.join()
consumer.join()
