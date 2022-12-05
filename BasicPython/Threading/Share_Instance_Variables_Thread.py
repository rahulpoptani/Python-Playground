
import threading

class CustomClass:
    def __init__(self):
        self.data = 10
        self.lock = threading.Lock()
    
    def task(self):
        with self.lock:
            self.data = 20
        print(f'Task: {self.data}')

cc = CustomClass()

for x in range(10):
    thread = threading.Thread(target=cc.task())
    thread.start()
