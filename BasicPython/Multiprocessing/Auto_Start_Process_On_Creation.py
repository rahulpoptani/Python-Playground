from time import sleep
from multiprocessing import Process

class AutoStartProcess(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start()

def task():
    print('Task Starting')
    sleep(1)
    print('Task Done')

if __name__ == '__main__':
    process = AutoStartProcess(target=task)
    process.join()