from time import sleep
from multiprocessing import Process, Event

def task(event):
    for i in range(10):
        sleep(1)
        if event.is_set():
            break
        print('Worker Process Running..', flush=True)
    print('Worker Closing Down', flush=True)

if __name__ == '__main__':
    event = Event()
    process = Process(target=task, args=(event,))
    process.start()
    sleep(3)
    print('Main Stopping Child Process')
    event.set()
    process.join()

