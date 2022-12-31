# Multiprocessing Manager provides a way of creating centralized Python objects that can be shared safely among processes.
# Manager objects create a server process which is used to host Python objects. Managers then return proxy objects used to interact with the hosted objects.
# The proxy objects automatically ensure process-safety and serialize data to and from the centralized objects.

# Managers provide three key capabilities for process-based concurrency, they are:
    # Centralized: A single instance of a shared object is maintained in a separate server process.
    # Process-safety: Proxy objects ensure that access to the centralized object is process-safe in order to avoid race conditions.
    # Pickability: Proxy objects can be pickled and shared with child processes such as arguments in process pools and items in queues.

# Using a manager involves four steps, they are:
    # Create the manager instance.
    # Start the manager.
    # Create one or more hosted objects to share.
    # Shutdown the manager.

# What Objects does a manager provides
    # Data structures: dict, list
    # Shared ctypes: Value, Array
    # Concurrency primitives: Lock, Event, Condition, Semaphore, BoundedSemaphore, Barrier
    # Queues: Queue, JoinableQueue
    # Other Objects: Namespace, Pool

# When to use Manager
# A manager should be used when an object needs to be shared among processes.
# Sometimes the object can be shared directly without problem, other times it cannot and a manager is required for those cases, which include:
    # When the shared object cannot be pickled and needs to be pickled in order to be shared.
    # When the shared object is not process-safe and needs to be used in multiple processes simultaneously

# Examples Where Manager is Required:
    # When sharing a concurrency primitive (e.g. lock, semaphore, event, etc.) or queue with a multiprocessing.Pool or concurrent.futures.ProcessPoolExecutor. This is because concurrency primitives cannot be pickled and all arguments to process pools must be pickled.
    # When sharing an object that cannot be pickled with processes via a multiprocessing.Queue. This is because the multiprocessing.Queue requires that all objects put on the queue be pickled.


from time import sleep
from random import random
from multiprocessing import Process, Manager

def task(number, shared_list):
    value = random()
    sleep(value)
    shared_list.append((number, value))

if __name__ == '__main__':
    with Manager() as manager:
        shared_list = manager.list()
        processes = [Process(target=task, args=(i, shared_list)) for i in range(50)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        print(f'List: {len(shared_list)}')



