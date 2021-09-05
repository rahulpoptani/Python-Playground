import os

print(os.getcwd())

os.chdir('/Users/r0p04cj/rahul/Personal/git/')

print(os.getcwd())

print(os.listdir())

os.mkdir('tempDir_deletethis')

print(os.listdir())

os.rmdir('tempDir_deletethis')

print(os.listdir())

# Create empty file
open('myfile.txt', 'w')

print(os.listdir())

# rename file
os.rename('myfile.txt', 'text_renamed.txt')

print(os.listdir())

print(os.stat('text_renamed.txt'))

# get file modification date
from datetime import datetime
mod_time = os.stat('text_renamed.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# Tree structure. all folders and files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path', dirpath)
    print('Current Directory', dirnames)
    print('Current Files', filenames)
    print()


print(os.environ.get('HOME'))

# Use path.join instead of concatenation 
print(os.path.join(os.environ.get('HOME'), 'file.txt'))

# Builtin functions
print(dir(os.path))

