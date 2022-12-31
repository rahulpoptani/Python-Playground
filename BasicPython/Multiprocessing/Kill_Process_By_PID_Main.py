# we may need to kill a process by its process identifier or PID
# This may be for many reasons, such as:
    # The task executed by the process is no longer required.
    # The process has had an error or is out of control.
    # The main program is closing down due to a user request.

# os.kill() takes two arguments. PID and Signal to send
# Example: os.kill(1234, signal.SIGKILL)

# The SIGINT or signal interrupt can be used to terminate the target process, which is equivalent to the user pressing CONTROL-C on the process. Alternately, the SIGKILL or signal kill process can be used to terminate the process forcefully.
# The difference between SIGINT and SIGKILL is that it is possible for a process to detect and handle a SIGINT, whereas a SIGKILL cannot be handled.

# Issues with Windows. Might work in Linux

from os import kill, getpid
from signal import SIGKILL

pid = getpid()

print(f'Running with pid: {pid}')

kill(pid, SIGKILL)

print('Process Killed')

