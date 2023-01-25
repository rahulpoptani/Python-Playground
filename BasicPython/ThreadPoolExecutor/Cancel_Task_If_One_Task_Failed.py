from time import sleep
from threading import Event
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_EXCEPTION

def work(event, name):
    for _ in range(10):
        sleep(1)
        if name == 0:
            print(f'task has failed, name={name}')
            raise Exception('Failed Task Exception')
        # check if task should stop
        if event.is_set():
            print(f'Stopping, name: {name}')
            return

event = Event()
with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(work, event, i) for i in range(10)]
    print('Waiting for task to complete or fail...')
    done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
    if len(done) > 0 and len(done) != len(futures):
        future = done.pop()
        if future.exception() != None:
            print(f'One task failed with: {future.exception()}, shutting down..')
            # cancel scheduled futures
            for future in futures:
                future.cancel()
            # stop running task
            event.set()
print('All Done')