# Daemon child processes are stopped by the parent process
# Recall: parent process will exit once all non-daemon child processes have terminated.
# The main parent process is a non-daemon process, so if it is the only non-daemon process running then the Python program will exit.
# This is still the case even if we have one or more daemon processes currently running.

from time import sleep
from multiprocessing import current_process, Process

# The idea is that the daemon process will not be able to complete its task before the main parent process terminates. 
# This will in turn cause the Python program to exit and abruptly terminate the daemon process in the middle of its task.

# perform long running task which it won't be able to complete on time before main finishes
def task():
    process = current_process()
    print(f'Daemon Process: {process.daemon}')
    for i in range(1000):
        print(i, flush=True)
        sleep(0.1)

if __name__ == '__main__':
    process = Process(target=task, daemon=True)
    process.start()
    # block the main parent process for a moment to allow the daemon process to make some progress on its task
    sleep(3)
    print('Main Process exiting..')