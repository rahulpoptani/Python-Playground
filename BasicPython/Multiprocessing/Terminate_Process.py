# If possible, try to close the process
# There are two methods to kills a process. Both methods will only terminate the target process and NOT the child process
    # Process.terminate()
    # Process.kill()


from time import sleep
from multiprocessing import Process

def task():
    while True:
        sleep(1)
        print('Worker Process Running..', flush=True)

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    sleep(5)
    # The parent process wakes up then forcefully terminates the child process.
    # The child process is stopped immediately. The parent process then carries on and then decides to stop.
    process.terminate() # or process.kill()
    print('Parent is continuing on..')