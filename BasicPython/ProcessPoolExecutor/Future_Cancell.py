from time import sleep
from concurrent.futures import ProcessPoolExecutor, wait

def work(time):
    sleep(time)

def main():
    with ProcessPoolExecutor(1) as executor:
        future1 = executor.submit(work, 2)
        print(f'First Task Running = {future1.running()}')
        future2 = executor.submit(work, 0.5)
        print(f'Second Task Running = {future2.running()}')
        was_cancelled = future2.cancel()
        print(f'Second Task Cancelled: {was_cancelled}')
        # wait for 2nd task to finish just in case if not cancelled
        wait([future2])
        print(f'Second Task Running = {future2.running()}, Cancelled = {future2.cancelled()}, Done = {future2.done()}')
        wait([future1])


if __name__ == '__main__':
    main()
