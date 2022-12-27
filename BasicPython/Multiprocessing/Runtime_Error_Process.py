# It is common to get a RuntimeError when starting a new Process in Python.
# Common in Windows and MacOS where default start method is "spawn" or "spawn" has been set as start method explicitly


from multiprocessing import Process

def task():
    print('Hello from Child Process', flush=True)

# removing __name__ check will raise Runtime Exception
# the check involves checking if the code is running in the top-level environment and only then, attempt to start a new process.
# This is called “protecting the entry point” of the program.
if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    process.join()

# Why Do We Need to Protect Entry Point?
    # The reason is because our Python script will be loaded and imported automatically for us by child processes.
    # This is required to execute our custom code and functions in new child processes.
    # If the entry point was not protected with an if-statement idiom checking for the top-level environment, then the script would execute again directly, rather than run a new child process as expected.
    # Protecting the entry point ensures that the program is only started once, that the tasks of the main process are only executed by the main process and not the child processes.

