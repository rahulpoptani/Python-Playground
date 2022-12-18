
# when performing operations on a variable we must aquire lock

from threading import Thread, Lock

class ThreadSafeCounter:
    def __init__(self):
        self._counter = 0
        self._lock = Lock()
    
    def increment(self):
        with self._lock:
            self._counter += 1
    
    def value(self):
        with self._lock:
            return self._counter

def task(counter):
    for _ in range(100000):
        counter.increment()

counter = ThreadSafeCounter()
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(counter.value())