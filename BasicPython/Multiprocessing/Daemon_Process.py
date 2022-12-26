# A daemon thread or a daemon process runs in the background.
# Daemon Process cannot create child process

# Daemon processes are helpful for executing tasks in the background to support the non-daemon processes in an application.
# Uses of daemon processes might include:
    # Background logging to file or database.
    # Background data retrieval, updates, refresh.
    # Background data storage to disk or database.

# Some properties of these background tasks might include:
    # Sporadic: Tasks that run only when specific conditions arise (e.g. ad hoc logging).
    # Periodic: Tasks that run after a consistent interval (e.g. data save/load every minute).
    # Long-Running: Tasks that run for the duration of the program (e.g. monitoring a resource).

# IMPORTANT
# The main parent process will terminate once all non-daemon processes finish, even if there are daemon processes still running. 
# Therefore, the code it executes must be robust to arbitrary termination, such as the flushing and closing of external resources like streams and files that may not be closed correctly.

# Daemon: A main parent process will exit if only daemon processes are running (or if no processes are running).
# Non-Daemon: A main parent process will not exit if at least one non-daemon process is running


from time import sleep
from multiprocessing import current_process, Process

def task():
    process = current_process()
    print(f'Daemon Process: {process.daemon}')

if __name__ == '__main__':
    process = Process(target=task, daemon=True)
    process.start()
    # if join is omitted then the new process will finish too soon and we won't see the print message. Join helps to wait until child process is finished
    process.join() 


