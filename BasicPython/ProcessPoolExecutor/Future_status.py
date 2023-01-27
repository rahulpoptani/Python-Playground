from time import sleep
from concurrent.futures import ProcessPoolExecutor, wait

def work():
    sleep(1)

def main():
    with ProcessPoolExecutor() as executor:
        future = executor.submit(work)
        print(f'Future running = {future.running()}, done = {future.done()}')
        wait([future])
        print(f'Future running = {future.running()}, done = {future.done()}')

if __name__ == '__main__':
    main()