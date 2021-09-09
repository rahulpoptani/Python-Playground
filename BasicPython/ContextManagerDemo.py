from contextlib import contextmanager
import os


# @contextmanager
# def open_file(file, mode):
#     try:
#         f = open(file, mode)        # Equivalent = open_file('sample_context_manager.txt', 'w')
#         yield f                     # Equivalent = f
#     finally:
#         f.close()                   # teardown

# with open_file('sample_context_manager.txt', 'w') as f:
#     f.write('Sample Text by Custom Context Manager')

# print(f.closed)


# Another approach assume we want to go inside a specific directory to do some work and come back to original directory
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield           # we won't be working with object inside context manager like in case of files, hence no object is yield
    finally:
        os.chdir(cwd)


with change_dir('DSA/HackerRank/Easy'):
    print(os.listdir())         # this will print all files inside destination

print(os.listdir())             # this will print files inside Current working directory as it came out after work

