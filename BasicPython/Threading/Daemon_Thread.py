# A special type of thread used for background tasks, called daemon thread.
# Daemon threads are helpful for executing tasks in the background to support the non-daemon threads in an application.
# Uses of daemon threads might include:
# 1. Background logging to file or database.
# 2. Background data retrieval, updates, refresh.
# 3. Background data storage to disk or database.

# Background tasks can be varied in type and specific to your application.
# 1. Sporadic: Tasks that run only when specific conditions arise (e.g. ad hoc logging).
# 2. Periodic: Tasks that run after a consistent interval (e.g. data save/load every minute).
# 3. Long-Running: Tasks that run for the duration of the program (e.g. monitoring a resource).

from time import sleep
from threading import current_thread
from threading import Thread

def task2():
    thread = current_thread()
    print(f'Daemon Thread2: {thread.daemon}')

def task():
    thread = current_thread()
    print(f'Daemon Thread1: {thread.daemon}')
    # new thread created frem daemon thread is also daemon thread
    new_thread = Thread(target=task2)
    new_thread.start()

# create thread
thread = Thread(target=task, daemon=True)
thread.start()
# block for a moment so daemon thread can run
sleep(0.5)
