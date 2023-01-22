# callbacks are always called, even if the task is cancelled or fails itself with an exception.
# A callback can fail with an exception and it will not impact other callback functions that have been registered or the task.
# The exception is caught by the thread pool, logged as an exception type message, and the procedure moves on. In a sense, callbacks are able to fail silently.

# Demo:

from time import sleep
from concurrent.futures import ThreadPoolExecutor, wait

def custom_callback1(future):
    raise Exception('Exception from Callback1')
    print('callback1 called')

def custom_callback2(future):
    print('callback2 called')

def work():
    sleep(1)
    return 'Task is done'

with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    future.add_done_callback(custom_callback1)
    future.add_done_callback(custom_callback2)
    result = future.result()
    sleep(0.1)
    print(result)