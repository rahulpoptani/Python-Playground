# This will also give the same result as Local defined inside the task function.
# Even if threading.local is shared, value intialize inside the thread using local
# are private to each thread and there is NO data sharing between threads

from time import sleep
import threading

def task(value, local):
    # store data
    local.value = value
    # block for a moment
    sleep(value)
    # retrieve value
    print(f'Stored Value: {local.value}')

# create local storage
local = threading.local()

threading.Thread(target=task, args=(1,local)).start()
sleep(0.5)
threading.Thread(target=task, args=(2,local)).start()
