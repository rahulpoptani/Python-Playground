from time import sleep
from multiprocessing import Manager, Event
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_EXCEPTION

def work(event, name):
    for _ in range(10):
        sleep(1)
        if name == 0:
            print(f'Task has failed, name = {name}')
            raise Exception('Failed Task')
        if event.is_set():
            print(f'Stopping, name = {name}')
            return

if __name__ == '__main__':
    with Manager() as manager:
        event = manager.Event()
        with ProcessPoolExecutor(10) as executor:
            futures = [executor.submit(work, event, i) for i in range(10)]
            print('Waiting for tasks to complete, or fail..')
            done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
            if len(done) > 0 and len(done) != len(futures):
                future = done.pop()
                if future.exception() != None:
                    print(f'One task failed with {future.exception()}, shutting down..')
                    for future in futures:
                        future.cancel()
                    event.set()
    print('All Done')