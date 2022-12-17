# We can get values from the queue.Queue by blocking but limited by a timeout.
# This allows a consumer thread to both block while waiting for values to arrive in the queue, 
# but also execute other tasks while busy waiting. 
# It may be more efficient than being busy waiting without any blocking calls.



from time import sleep
from random import random
from threading import Thread
from queue import Queue, Empty

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
    queue.put(None)
    print('Producer Done')

# consume work
def consumer_func(queue: Queue):
    print('Consumer Running..')
    while True:
        try:
            item = queue.get(timeout=0.5)
        except Empty:
            print('Consumer gave up waiting')
            sleep(0.5)
            continue
        if item is None:
            break
        print(f'Got: {item}')
    # all done
    print('Consumer Done')

queue = Queue()
consumer = Thread(target=consumer_func, args=(queue,))
consumer.start()
producer = Thread(target=producer_func, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()