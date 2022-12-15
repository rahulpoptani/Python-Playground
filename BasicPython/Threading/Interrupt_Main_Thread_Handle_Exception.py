# interrupt the main thread and handle the interrupt with a try-except pattern.

from time import sleep
from threading import Thread
from _thread import interrupt_main
import sys

def task():
    sleep(3)
    print('Interrupting main thread now')
    interrupt_main() # a sub thread can use this method to interrupt main thread

thread = Thread(target=task)
thread.start()
try:
    while True:
        print('Main thread waiting...')
        sleep(0.5)
except KeyboardInterrupt:
    print('Main Interrupted! Exiting.')
    sys.exit()
