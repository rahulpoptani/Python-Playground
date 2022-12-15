# automatically start a new thread.

from threading import Thread
from time import sleep

class AutoStartThread(Thread):
    # new thread will start once initialize
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start()

def task():
    print('Task Starting')
    sleep(1)
    print('Task done')

thread = AutoStartThread(target=task)
thread.join()