from time import sleep
from threading import Thread
from threading import Event

def task(event: Event):
    # run until the event is set
    while not event.is_set():
        sleep(2)
        # perform task
        print('Background performing task')
    print('Background done')

# prepare state for stopping the background
stop_event = Event()

# create and start the background thread
thread = Thread(target=task, args=(stop_event,), daemon=True, name='Background')
thread.start()

# run main thread for a while
print('Main thread running...')
sleep(10)
print('Main thread stopping')
# request background thread to stop
stop_event.set()
# wait for the background thread to stop
thread.join()
print('Main done')