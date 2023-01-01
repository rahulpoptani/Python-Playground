# An asyncio Task is an object that schedules and independently runs an asyncio coroutine.
# A task is created from a coroutine. It requires a coroutine object, wraps the coroutine, schedules it for execution, and provides ways to interact with it.
# A task is executed independently. This means it is scheduled in the asyncio event loop and will execute regardless of what else happens in the coroutine that created it. 
# This is different from executing a coroutine directly, where the caller must wait for it to complete.

# There are 3 main ways you can create an asyncio Task from a coroutine, they are:
    # Create a Task with asyncio.create_task() (recommended)
    # Create a Task with asyncio.ensure_future() (low-level)
    # Create a Task with loop.create_task() (low-level)

# Creating a task does a few things.
    # It wraps the provided coroutine in an asyncio.Task instance.
    # It schedules the task (wrapped coroutine) for execution in the event loop.
    # It returns a Task instance that provides a handle on the scheduled coroutine.

import asyncio

async def task_coroutine(number):
    print(f'executing the task {number}')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    tasks = [asyncio.create_task(task_coroutine(i)) for i in range(20)]
    for task in tasks:
        await task
    print('main coroutine ended')

# Only one task executes at a time and sequentially in order. This is because the tasks were scheduled sequentially and the event loop is honoring the scheduling order.
asyncio.run(main())

