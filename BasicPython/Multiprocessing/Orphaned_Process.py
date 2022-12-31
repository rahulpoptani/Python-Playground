# An orphan process is created when the parent of a child process is terminated.

# Some ways that a parent process may be terminated leaving the child process orphaned include:
    # Parent process finishes.
    # Parent raises an uncaught error or exception.
    # Parent process calls sys.exit() or os._exit().
    # The Process.terminate() or Process.kill() methods are called on the parent.
    # A process calls os.kill() with the parent’s PID.
    # Process is killed externally, e.g. via the kill command.

# If a process is orphaned, it can be difficult to programmatically get a handle on it.
# In turn, it can be challenging to query the status of orphaned processes or to terminate them.

# Some solutions could be:
    # Other processes keep a reference to processes that could be orphaned, e.g. Process instances.
    # Store process identifiers (PIDs) for child processes that could be orphaned, e.g. in a file.
    # Child processes can check if they are orphaned and take action accordingly.

from time import sleep
from multiprocessing import Process, parent_process

def is_orphan():
    parent = parent_process()
    if parent is None or not parent.is_alive():
        return True
    return False

def level2():
    print(f'Orphaned: {is_orphan()}', flush=True)
    sleep(3)
    print(f'Orphaned: {is_orphan()}', flush=True)

def level1():
    Process(target=level2).start()

if __name__ == '__main__':
    process = Process(target=level1)
    process.start()
    sleep(1)
    process.terminate()
