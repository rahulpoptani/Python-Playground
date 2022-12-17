# we often need to monitor a resource and take action if a problem is detected.
# This may be for many reasons, such as:
    # Access to the resource is essential to the application.
    # The resource may be known to have rare but repeating intermittent problems.
    # The resource may be restarted or changed if there is a fault, allowing the application to continue working.
# This can be achieved using a watchdog thread


from time import sleep
from random import random
from threading import Thread

# task for worker thread
def worker_task():
    counter = 0
    while True:
        counter += 1
        print(f'Worker: {counter}')
        # conditionally fail
        if random() < 0.3:
            print('Worker Failed')
            break
        sleep(1)

# create and start a worker thread, returns instance of thread
# This function can be used to initially start the worker thread, and to restart the worker thread if it fails.
def boot_worker():
    # create and configure the thread
    worker = Thread(target=worker_task, name='Worker')
    worker.start()
    # return instance of thread
    return worker

# task for watchdog thread
# The watchdog will poll the worker thread every half second.
def watchdog_func(target, action):
    print('Watchdog Thread')
    while True:
        # check status of target thread
        if not target.is_alive():
            print('Watchdog: target thread is not running, restarting...')
            target = action()
        sleep(0.5)

worker = boot_worker()
watchdog = Thread(target=watchdog_func, args=(worker, boot_worker), daemon=True, name='Watchdog')
# start watching
watchdog.start()
# the main thread is free to go off and run the main application.
# do other things
watchdog.join()

