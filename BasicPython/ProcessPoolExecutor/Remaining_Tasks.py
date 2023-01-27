from time import sleep
from concurrent.futures import ProcessPoolExecutor, as_completed

def task():
    sleep(1)

def main():
    with ProcessPoolExecutor(4) as executor:
        futures = [executor.submit(task) for _ in range(50)]
        print('Waiting for task to complete')
        for _ in as_completed(futures):
            print(f'About {len(executor._pending_work_items)} task remains')

if __name__ == '__main__':
    main()