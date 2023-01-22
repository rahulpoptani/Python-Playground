# Use the exception method to check if the exception is raised

from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait

def custom_callback(future):
    print(f'Custom Callback Called')

def work():
    sleep(1)
    raise Exception('Dummy Exception')

with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    future.add_done_callback(custom_callback)
    wait([future])
    running = future.running()
    cancelled = future.cancelled()
    done = future.done()
    print(f'Task Running: {running}, cancelled: {cancelled}, done: {done}')
    exception = future.exception()
    print(f'Exception: {exception}')
    try:
        result = future.result()
    except:
        print('Unable to get result')