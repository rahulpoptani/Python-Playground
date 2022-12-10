
from time import sleep
import threading

def work():
    print('New Thread: Working..')
    sleep(1)
    # raise exception
    raise Exception('Something broke')

# custom exception hook
def custom_hook(args):
    # report the failure
    print(f'New Thread Failed: {args.exc_value}')

# set the exception hook
threading.excepthook = custom_hook

# create and start thread
thread = threading.Thread(target=work)
thread.start()
# wait for thread to finish
thread.join()
# continue on
print('Main: Continuing on...')