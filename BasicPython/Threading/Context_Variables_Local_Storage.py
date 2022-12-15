# Context variables were created to provide thread-local-like storage that works 
# the same way in threads and in coroutines.
# As such, contextvars were primarily developed for use with asyncio.
# Nevertheless, they can be used with Python thread as well for consistency.

# Difference: Thread-Local Storage only works per-thread, whereas context variables work per thread or per coroutine.


from random import random
from time import sleep
from threading import Thread
from contextvars import ContextVar

def color_report():
    global color
    sleep(random())
    print(f'The color is {color.get()}')

def task(color_arg):
    global color
    color.set(color_arg)
    color_report()

# define global state
color = ContextVar('color', default='unknown')
colors = ['red','green','blue','yellow','orange','purple']
threads = [Thread(target=task, args=(col,)) for col in colors]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

