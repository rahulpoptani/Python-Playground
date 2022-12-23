# You can reduce lock contention using lock splitting.
# Lock splitting is a technique for reducing lock contention.
# It involves increasing the granularity of the usage of mutex locks in your application.

# Coarse lock granularity means that one lock protects many state variables or resources, whereas fine lock granularity means that one lock protects few state variables or resources.
    # Coarse Lock Granularity: One lock protects many variables.
    # Fine Lock Granularity: One lock protects a few variables.

# Lock granularity can be increased via lock splitting.

# Split By Code: Split one lock into multiple locks based on the specific objects, variables, and functions you have in your code.
# Split By Functionality: Split one lock into multiple locks based on the specific roles and responsibilities within the application


# Lock Splitting by Variables:
# ==============================

# a = list()
# b = 0
# c = dict()

# Instead of single lock, multiple lock should be used on non-depended variables. If we have used single lock at
# both the below operations of append and dict update, then once first lock was release then only we should be able to
# do operations on dictionary. With separate locks this operations are independent
# Example:

# lock1 = Lock()
# lock2 = Lock()

# with lock1:
    # a.append('some value')

# with lock2:
#     b += 1
#     c[b] = 0

# Lock Splitting by Functionality:
# ==================================

# lock_read = Lock()
# lock_write = Lock()

# def read(resource, lock):
#     with lock:
#         resource.read()

# def write(resource, lock):
#     with lock:
#         resource.write()

# resource = "some resource"

# read(resource, lock_read)
# write(resource, lock_write)


# Example:
# Each thread then executes its task look five times and randomly performs a read or write operation.
# The task will use a separate lock for read operations from write operations. This means that only a subset of threads will contend for a lock based on the specific subtask being performed, rather than a single lock used to protect the shared data.

from random import random
from time import sleep
from threading import Thread, Lock

def read_subtask(data, lock, identifier):
    with lock:
        sleep(random())
        print(f'Thread {identifier} read {data}')

def write_subtask(data, lock, identifier):
    with lock:
        sleep(random())
        data.append(identifier)
        print(f'Thread {identifier} wrote to data')

def task(data, read_lock, write_lock, identifier):
    for _ in range(5):
        if random() < 0.5:
            read_subtask(data, read_lock, identifier)
        else:
            write_subtask(data, write_lock, identifier)

data = list()
read_lock = Lock()
write_lock = Lock()

threads = [Thread(target=task, args=(data, read_lock, write_lock, i)) for i in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
