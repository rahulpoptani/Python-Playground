import threading
import time

def task(argument):
    for _ in range(3):
        time.sleep(1)
        print(f'From task {argument} slept: {_}')

# create new thread and ask to run a method
thread = threading.Thread(target=task, args=('something',))

# run the thread - start() function on a new thread will call the run() function. The run() function will in turn call your custom function if specified via the "target" keyword
# start() does not block
thread.start()

print('This will print immediately and will not wait for the thread to finish')

# check if the thread is alive?
print(f'Thread is live? {thread.is_alive()}')

# wait for the thread to finish
thread.join()
print('Thread finished')

# check if the thread is alive?
print(f'Thread is live? {thread.is_alive()}')

# Notes:
# You share between threads using queue.Queue