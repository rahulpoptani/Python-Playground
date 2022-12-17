# Python code is compiled at runtime into Python bytecode and executed in the Python virtual machine.
# The Python bytecodes are executed using a stack data structure that adds instructions as functions are called and pops instructions as they are executed
# Each Python thread will have its own stack of instructions that are maintained and executed.
# The size of the stack is fixed and is pre-allocated by the Python interpreter for each thread.

# We may want to change the Python thread stack size in our program.
# For example, we may have a large number of very simple worker threads that execute a single function with few local variables. In that case, we may want to set the thread stack size to the minimum value.
# More likely, we may have one or more worker threads executing complex function call graphs. This might involve many small functions with many local variables and perhaps some functions called recursively


from threading import stack_size

size = stack_size()
# we can see that the value of zero is returned and reported, which indicates that the default for the operating system is being used.
print(size)

old_size = stack_size(32768)
print(old_size) # return 0
size = stack_size()
print(size) # return 32768

# The thread stack size must be specified before new threads are created for those threads to take on the new value.
# The minimum value for the “size” argument is 32 kilobytes (kb) which is 32,768 bytes.
# Most operating systems impose a constraint on the value of the “size” argument that it must be a multiple of 4,096 bytes.

# The thread stack size can be increased by specifying a value that is a multiple of 4,096 bytes and larger than 32 kilobytes (kb) which is 32,768 bytes.

# Common values might include

#     4,096 * 8 = 32,768 bytes
#     4,096 * 16 = 65,536 bytes
#     4,096 * 32 = 131,072 bytes
#     4,096 * 64 = 262,144 bytes
#     4,096 * 128 = 524,288 bytes

