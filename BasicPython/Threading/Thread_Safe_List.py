# Many common operations on a list are atomic, meaning that they are thread-safe.
# Operations such as adding, removing, and reading a value on a list are atomic.
# Specifically:
    # Appending a value via append().
    # Adding a list to a list via extend().
    # Assigning multiple values of a list via a slice.
    # Getting a value from a list via bracket notation [].
    # Removing the last value from a list via pop().
    # Sorting a list via sort().
# Above is only true at the time of writing

# A list can be made thread-safe using a mutual exclusion (mutex) lock
# Specifically, each add, delete, update, and read of the list must be protected by a lock.
# This can be achieved by wrapping a list with a new class. The class can then expose 
# the specific operations that we require on the list and protect those operations on the internal list using a lock.

# define a new class with the same interface as the List class, except the functions on the class are threads-safe.

# Creating new thread safe class like below have risk and more code to write, instead use Queue

from threading import Lock, Thread

class ThreadSafeList():
    def __init__(self):
        self._list = list()
        self._lock = Lock()
    def append(self, value):
        with self._lock:
            self._list.append(value)
    def pop(self):
        with self._lock:
            return self._list.pop()
    def get(self, index):
        with self._lock:
            return self._list[index]
    def length(self):
        with self._lock:
            return len(self._list)

def add_items(safe_list):
    for i in range(100000):
        safe_list.append(i)

safe_list = ThreadSafeList()
threads = [Thread(target=add_items, args=(safe_list,)) for _ in range(10)]
for thread in threads:
    thread.start()
print('Main waiting for all threads')
for thread in threads:
    thread.join()
print(f'List size: {safe_list.length()}')