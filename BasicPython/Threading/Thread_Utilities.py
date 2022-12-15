# threading related utilities function goes here

import threading
import time
# report the number of active threads
count = threading.active_count()
print(f'Number of active threads: {count}')

def task():
    time.sleep(1)
    new_thread = threading.current_thread()
    ident = threading.get_ident()
    native_id = threading.get_native_id()
    print(f'Name of new thread: {new_thread.name} with identifier: {ident} with OS identifier: {native_id}')
    print(f'Deamon: {thread.daemon} isAlive: {thread.is_alive()}')

thread = threading.Thread(target=task)
thread.start()

# get all active threads
for threads in threading.enumerate():
    print(f'Currently active thread: {threads.name}')

count = threading.active_count()
print(f'Number of active threads: {count}')

thread.join()

count = threading.active_count()
print(f'Number of active threads: {count}')