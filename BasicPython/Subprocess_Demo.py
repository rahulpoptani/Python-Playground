import subprocess

# list all files and folder in current working directory
# If shell argument is omited, we cannot provide extended command like -la, instead need to pass only ls
subprocess.run('ls -la', shell=True)

# In order to send both ls and -ls without shell=True, we need to pass all the argument as list
subprocess.run(['ls', '-la'])

p1 = subprocess.run(['ls', '-la'])
print(p1.args)
print(p1.returncode) 

# When running the subprocess command, it will automatically print the output, in order to capture
p1 = subprocess.run(['ls', '-la'], capture_output=True)
# The output of p1.stdout is binary, need to decode to make it look pretty
print(p1.stdout.decode())

# alternate to decode is
p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(p1.stdout)

# To redirect the output to a file
with open('output.txt', 'w') as file:
    p1 = subprocess.run(['ls', '-la'], stdout=file, text=True)


# Chaining output to another subprocess

p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
print(p1.stdout)
p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# or use with shell true and take as one complete command
p1 = subprocess.run('cat output.txt | grep -n test', capture_output=True, text=True, shell=True)
print(p1.stdout)