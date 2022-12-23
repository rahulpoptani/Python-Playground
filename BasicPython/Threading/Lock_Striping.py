# One approach to reducing contention is called lock striping.
# It is used when a lock is used to protect a data structure such as a list or hash map.
# The lock protecting the data structure is split into multiple locks, each protecting a subset of the data in the data structure.

# Lock striping can be implemented using a list of locks.
# A list of locks can be created and used to protect a data structure that is accessed using an array index, such as a list. It could be used for a dict, but may require a custom implementation.

# The more locks in the list, the less contention there will be for the data being protected, although the more memory required
# Example:
# If we had five locks, then each lock could protect 1/5 (one fifth) of the data in the structure. If the structure was a list with 100 items, then:
    # Lock 0 could protect indexes in the list from 0 to 19.
    # Lock 1 could protect indexes in the list from 20 to 39.
    # Lock 2 could protect indexes in the list from 40 to 59.
    # Lock 3 could protect indexes in the list from 60 to 79.
    # Lock 4 could protect indexes in the list from 80 to 99.


from random import randint, random
from time import sleep
from threading import Thread, Lock

def task(identifier, locks, data_list):
    # decide where to operate on the list
    index = randint(0, len(data_list)-1)
    # map array index to lock index
    lock_index = index % len(locks)
    # aquire the lock
    with locks[lock_index]:
        # do some work, block for a while
        sleep(random())
        data_list[index] += 1
        print(f'Thread {identifier} updated index {index} to {data_list[index]}')

# create shared locks
locks = [Lock() for _ in range(5)]
# create shared data
data_list = [0 for _ in range(20)]
# create threads
threads = [Thread(target=task, args=(i, locks, data_list)) for i in range(20)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(data_list)
