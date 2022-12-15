# This can be achieved by defining a new function to handle the interruption and 
# registering this function to be called to handle the SIGINT when it occurs.
# we must define a new function to handle the SIGINT. This function must take the signal number and the current stack frame as arguments.


from time import sleep
from threading import Thread
from _thread import interrupt_main
from signal import signal
from signal import SIGINT
import sys

def handle_sigint(signalnum, frame):
    print('Main Interrupted! Exiting.')
    sys.exit()

def task():
    sleep(3)
    print('Interrupting main thread now')
    interrupt_main() # a sub thread can use this method to interrupt main thread

# we can register our function to handle the SIGINT via the signal
signal(SIGINT, handle_sigint)
thread = Thread(target=task)
thread.start()

while True:
    print('Main thread waiting...')
    sleep(0.5)

