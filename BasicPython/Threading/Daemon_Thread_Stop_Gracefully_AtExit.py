# when using threading.Event to stop the thread, a manual interventionb is required by the main thread
# we can automate this and leave the main thread free to focus on the main task of the application
# we can have a python function called by the python process automatically just prior to the process terminating.
# the capability is provided by the atexit module

from time import sleep
from threading import Thread
from threading import Event
import atexit

# background task
def task(event: Event):
    # run forever
    while not event.is_set():
        sleep(2)
        # perform task
        print('Background performing task')
    print('Background done')

# stop the background task gracefully before exit
def stop_background(stop_event: Event, thread: Thread):
    print('AtExit Stopping')
    # request the background thread to stop
    stop_event.set()
    # wait for the background thread to stop
    thread.join()
    print('AtExit Done')

# prepare state for stopping the background
stop_event = Event()

# create and start background thread
thread = Thread(target=task, args=(stop_event,), daemon=True, name='Background')
thread.start()

# register the at exit
# this means whenever main thread want to stop the daemon thread, just call the stop_background method
atexit.register(stop_background, stop_event, thread)

# run main thread for a while
print('Main thread running...')
sleep(10)
print('Main thread stopping..')
