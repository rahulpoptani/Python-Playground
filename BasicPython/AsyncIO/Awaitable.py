# A coroutine is an awaitable that can be wrapped in a Task. A coroutine can pause execution and wait for an awaitable object to be done via the await keyword.
# An awaitable is a Python object that can be waited on using the “await” keyword

# An awaitable allows a coroutine in asyncio to pause execution and wait for the specified awaitable to be done.

# There are three main types of awaitables that may work within our asyncio programs, they are:
    # Coroutine
    # Future
    # Task

# Coroutines are awaitable, which means that a coroutine may wait on another coroutine.
# A task is a coroutine that is wrapped and executed independently. May also wait for it to complete.
# The Task class extends the Future class, which is also awaitable. 

# There are two main ways to create an awaitable, they are:
    # Create a Coroutine
    # Create a Task

# Example: 
    # Running the example first creates the custom coroutine, then uses it to start the asyncio event loop.
    # The coroutine executes and reports a message. I then create a second coroutine and schedule it for execution. This pauses the execution of the first coroutine until the second coroutine is done.

import asyncio
async def another_coroutine():
    print('Another Coroutine')

async def custom_coroutine():
    print('Hello World')
    await another_coroutine()

asyncio.run(custom_coroutine())

# Example: 
    # we will run a coroutine that will create a second coroutine that will be wrapped in a task. The first coroutine will then await the task, treating it directly as an awaitable.

import asyncio
async def another_coroutine():
    print('Another Coroutine')

async def custom_coroutine():
    print('Hello World')
    await asyncio.create_task(another_coroutine())

asyncio.run(custom_coroutine())
