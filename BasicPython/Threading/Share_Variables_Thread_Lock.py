# when sharing adhoc variables between threads, a mutual exclusive lock (mutex) can be used
# A lock can be used to protect one or multiple shared variables of any type.
# The shared variables will be protected from race conditions as long as all access and changes to the variables are protected by the lock.
# Each thread interested in the variable must first aquire the lock, and then release it once they are finished with the variable.
# A thread trying to aquire a lock that has already been aquired must wait until the lock has been released again.

# Ways to aquire lock
# 1. Using Context Manager: with lock:
# 2. lock = Lock(); lock.aquire(); lock.release()
# 3. lock.aquire(blocking=false) # if the lock cannot be aquire than false is returned, it won't wait for the lock
# 4. lock.aquire(timeout=10) # wait the set number of seconds to aquire lock before giving up. If the lock cannot be aquire it will return false


import threading
import time
from random import random

def task(lock: threading.Lock, identifier, value):
    # aquire the lock:
    with lock:
        print(f'thread {identifier} got the lock, sleeping for {value}')
        time.sleep(value)

# create a shared lock
lock = threading.Lock()

# start few threads to execute the same critical section
for i in range(10):
    # start the thread
    threading.Thread(target=task, args=(lock, i, random())).start()

# wait for all thread to finish