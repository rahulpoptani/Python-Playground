
# Is the Queue Thread-Safe?
# Yes.
# The queue.Queue class is thread-safe.
# This means that multiple threads may call get() and/or put() concurrently and the internal state of the queue will be maintained correctly without corruption.
# It also means that queries of the queue like qsize(), empty() and full() will report the correct state of the queue at the time of the function call.

from queue import Queue, Full, Empty

# Queue can have a maxsize argument
queue = Queue(maxsize=5)

# put() method will block if queue is full and wait until queue is poped
for x in range(6):
    # queue.put(x) # this will block forever after inserting 5 elements and waiting to ingest 6th element
    try:
        # queue.put_nowait(x) # this will not block, and if full will simple raise queue.Full exception
        # queue.put(x, timeout=2) # this will block only until timeout to wait for other thread to pop the element, after timeout it will raise queue.Full exception
        queue.put(x, block=False) # adding block=False will avoid blocking and will raise queue.Full exception
    except Full:
        print('Queue Full')

print(f'Is the Queue Full: {queue.full()} with size: {queue.qsize()}')

for x in range(6):
    # queue.get() this will block forever because its a blocking call. After poping 5 element it will try to pop an empty queue and will wait forever.
    try:        
        # queue.get_nowait() # equivalent to get with block=False, will raise queue.Empty exception
        # queue.get(timeout=3) # will wait for configured seconds and will then raise the exception
        queue.get(block=False) # this will not wait and raise queue.Empty exception
    except Empty:
        print('Queue Empty')

print(f'Is the Queue Empty: {queue.empty()} with size: {queue.qsize()}')

# Note, the state of the queue may change immediately after any of these queries, so care must be taken to avoid a race condition.
# Example: This is NOT thread safe
# if not queue.full():
#     queue.put_nowait(123)

# NOT recommended, but this is thread safe
# with queue.mutex:
#     if not queue.full():
#         queue.put_nowait(123)

