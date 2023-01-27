from random import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def thread_work(process_id, thread_id):
    value = random()
    sleep(value)
    print(f'Process {process_id}, thread {thread_id}, value {value}', flush=True)
    return value

def process_work(identifier):
    with ThreadPoolExecutor() as exe:
        total = sum(exe.map(thread_work, [identifier]*5, range(5)))
    print(f'Process {identifier} Done, total {total}', flush=True)
    return total

if __name__ == '__main__':
    with ProcessPoolExecutor() as exe:
        total = sum(exe.map(process_work, range(5)))
    print(f'Main done, total = {total}', flush=True)