
from time import sleep
from multiprocessing import Process
from signal import signal, SIGTERM
import sys

def handler(sig, frame):
    print('Child process cleaning up..', flush=True)
    sleep(2)
    sys.exit(0)

def task():
    signal(SIGTERM, handler)
    while True:
        sleep(1)
        print('Worker Process Running..', flush=True)

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    sleep(5)
    process.terminate() # or process.kill()
    print('Parent is continuing on..')