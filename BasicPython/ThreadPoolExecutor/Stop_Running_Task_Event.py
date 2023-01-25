from time import sleep
from threading import Event
from concurrent.futures import ThreadPoolExecutor

def work(event):
    for _ in range(100):
        sleep(1)
        if event.is_set():
            print('Not done, asked to stop')
            return
    return 'All done from task'

event = Event()
executor = ThreadPoolExecutor(5)
futures = [executor.submit(work, event) for _ in range(50)]
print('Task is running..')
sleep(2)
print('Cancelling all task')
# this will cancel all task which are still in queue and in scheduled state and not running state
for future in futures:
    future.cancel()
print('Trigerring all running task to stop')
event.set()
print('Shutdown executors...')
executor.shutdown()