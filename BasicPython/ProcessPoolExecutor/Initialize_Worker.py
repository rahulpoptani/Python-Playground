from time import sleep
from concurrent.futures import ProcessPoolExecutor

def initialize_worker():
    print(f'Initializing worker process', flush=True)

def task(identifier):
    sleep(1)
    return identifier

def main():
    with ProcessPoolExecutor(max_workers=2, initializer=initialize_worker) as executor:
        for result in executor.map(task, range(10)):
            print(result)

if __name__ == '__main__':
    main()