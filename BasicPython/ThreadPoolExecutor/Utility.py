# Get name of threads
import threading
from concurrent.futures import ThreadPoolExecutor

def task(number):
    pass

executor = ThreadPoolExecutor(thread_name_prefix='TaskPool')
executor.map(task, range(10))
for thread in threading.enumerate():
    print(thread.name)
executor.shutdown()


