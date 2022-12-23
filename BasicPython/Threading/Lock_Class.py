# A class may also have class variables and class methods defined with the @classmethod decorator.
# Instance creation is not required here, Class methods can variables can be directly access
from threading import Thread, Lock

class ThreadSafeClass:
    lock = Lock()
    counter = 0
    
    @classmethod
    def increment(cls):
        with cls.lock:
            cls.counter += 1
    
    @classmethod
    def report(cls):
        with cls.lock:
            print(cls.counter)

def task():
    for i in range(10000):
        ThreadSafeClass.increment()

threads = [ Thread(target=task) for _ in range(1000) ]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

ThreadSafeClass.report()
