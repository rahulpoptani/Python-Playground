# Shared ctypes provide a mechanism to share data safely between processes in a process-safe manner.
# The ctypes module provides tools for working with C data types.

# Python provides the capability to share ctypes between processes on one system.
# This is primarily achieved via the following classes:
    # multiprocessing.Value: manage a shared value.
    # multiprocessing.Array: manage an array of shared values.

# A shared ctype value can be defined in a parent process, then shared with multiple child processes. 
# All child processes and the parent process can then safely read and modify the data within the shared value.

# This can be useful in number of cases:
    # A counter shared among multiple processes.
    # Returning data from a child process to a parent process.
    # Sharing results of computation among processes.

# the multiprocessing.Value makes use of a multiprocessing.RLock
# NOTE when modifying. The Value class have mutex lock and below approach should be used. Same with Array class
# with variable.get_lock():
#     variable.value += 1

# Data types must be specified when using a multiprocessing.Value or multiprocessing.Array.

# import ctypes
# typecode_to_type = {
#     'c': ctypes.c_char, 'u': ctypes.c_wchar,
#     'b': ctypes.c_byte, 'B': ctypes.c_ubyte,
#     'h': ctypes.c_short, 'H': ctypes.c_ushort,
#     'i': ctypes.c_int, 'I': ctypes.c_uint,
#     'l': ctypes.c_long, 'L': ctypes.c_ulong,
#     'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
#     'f': ctypes.c_float, 'd': ctypes.c_double
#     }

from random import random, randint
from multiprocessing import Process, Value, Array

def task(variable):
    variable.value = random()
    print(f'Written By Child: {variable.value}', flush=True)

def task2(variable):
    for i in range(len(variable)):
        variable[i] = randint(0,100)
    data = [item for item in variable]
    print(f'Written by Child: {data}', flush=True)

if __name__ == '__main__':
    # Example: Using Value
    # The first argument defines the data type for the value. It may be a string type code or a Python ctype class. The second argument may be an initial value.
    variable = Value('f', 0.0)
    process = Process(target=task, args=(variable,))
    process.start()
    process.join()
    print(f'Read By Main: {variable.value}')

    # Example: Using Array
    array_variable = Array('i', (1,2,3,4))
    data = [item for item in array_variable]
    print(f'Initialized: {data}')
    process1 = Process(target=task2, args=(array_variable,))
    process1.start()
    process1.join()
    data = [item for item in array_variable]
    print(f'Read: {data}')


