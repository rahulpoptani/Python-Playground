from time import sleep
from concurrent.futures import ThreadPoolExecutor

def task(number):
    sleep(1)
    return number

def custom_callback1(future):
    print(f'callback1: {future.result()}')

def custom_callback2(future):
    print(f'callback2: {future.result()}')

with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in futures:
        future.add_done_callback(custom_callback1)
        future.add_done_callback(custom_callback2)

# Note: Callback gets executed as soon as: 
# 1. task is done
# 2. cancel the task before execution
# 3. exception is raised by task