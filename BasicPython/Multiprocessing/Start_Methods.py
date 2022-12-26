# Typees of start methods
    # spawn: start a new Python process.
    # fork: copy a Python process from an existing process.
    # forkserver: new process from which future forked processes will be copied.

# The following lists the major platforms and the start methods that are supported.
    # Windows (win32): spawn
    # macOS (darwin): spawn, fork, forkserver.
    # Linux (unix): spawn, fork, forkserver.

import multiprocessing

# The function returns a list of string values, each representing a supported start method.
methods = multiprocessing.get_all_start_methods()

print(f'All Start methods supported by OS: {methods}')

print(f'Current Start Method: {multiprocessing.get_start_method()}')

if __name__ == '__main__':
    # To set a start method
    # multiprocessing.set_start_method('spawn') # Raise Exception
    # current start method
    print(multiprocessing.get_start_method())

# this will not work on windows. Getting context
# context = multiprocessing.get_context('fork')
