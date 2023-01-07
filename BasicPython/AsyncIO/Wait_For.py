# You can wait for an asyncio task or coroutine to complete with a timeout using the asyncio.wait_for() function.
# If the timeout elapses before the task completes, the task is canceled.
# If no timeout is specified, the wait_for() function will wait until the task is completed.

# This allows the caller to both sets an expectation about how long they are willing to wait for a task to complete, and to enforce the timeout by canceling the task if the timeout elapses.

# The wait_for() function returns a coroutine that is not executed until it is explicitly awaited or scheduled as a task.
# If a coroutine is provided, it will be converted to the task when the wait_for() coroutine is executed.

# If the timeout elapses before the task is completed, the task is canceled, 
# and an asyncio.TimeoutError is raised, which may need to be handled.

# The asyncio.wait_for() function does not block. Instead, it returns a coroutine.

# Example: No Timeout

from random import random
import asyncio

async def task_coro(arg):
    value = random()
    print(f'task got {value}')
    await asyncio.sleep(value)
    print('task done')

async def main():
    task = task_coro(1)
    await asyncio.wait_for(task, timeout=None)

asyncio.run(main())

