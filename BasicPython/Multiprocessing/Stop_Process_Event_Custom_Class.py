from time import sleep
from multiprocessing import Process, Event

class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.event = Event()

    def run(self):
        for i in range(10):
            sleep(1)
            if self.event.is_set():
                break
            print('Worker Process Running..', flush=True)
        print('Worker Closing Down', flush=True)

if __name__ == '__main__':
    process = CustomProcess()
    process.start()
    sleep(3)
    print('Main Stopping Child Process')
    process.event.set()
    process.join()

