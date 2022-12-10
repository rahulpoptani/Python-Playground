# Sometimes we may need to store data that is unique for each thread.
# Python provides a thread-local object that can be used to store unique data 
# for each thread. The thread-local storage provides an alternative to having 
# to extend the threading.Thread class and define instance variables for thread-specific data.

# Data stored and retrieved on the thread-local object may have the 
# same variable names across threads, meaning the same code can be used 
# across threads, a common approach when using worker threads.

# Importantly, the reads and writes to the thread-local object are unique and private at the thread-level

from time import sleep
import threading

def task(value):
    # create local storage
    local = threading.local()
    # store data
    local.value = value
    # block for a moment
    sleep(value)
    # retrieve value
    print(f'Stored Value: {local.value}')

# use dictionary data structure
def task2(value):
    local = threading.local()
    local.values = {value: "ABC"}
    sleep(value)
    print(f'Stored Value: {local.values}')

threading.Thread(target=task2, args=(1,)).start()
sleep(0.5)
threading.Thread(target=task2, args=(2,)).start()


