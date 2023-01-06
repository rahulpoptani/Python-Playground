# We may need to get access to all tasks in an asyncio program.
# This may be for many reasons, such as:
    # To introspect the current status or complexity of the program.
    # To log the details of all running tasks.
    # To find a task that can be queried or canceled.

# The task has been scheduled but is not yet running.
# The task is currently running (e.g. but is currently suspended)

import asyncio

async def task_couroutine(value):
    print(f'task {value} is running')
    await asyncio.sleep(1)

async def main():
    print('Main coroutine started')
    # start many task. This will start 10 task
    started_task = [asyncio.create_task(task_couroutine(i)) for i in range(10)]
    # Allow some of the task time to start
    await asyncio.sleep(0.1)
    tasks = asyncio.all_tasks() # including main task = main task + 10 started task
    for task in tasks:
        print(f'{task.get_name()} {task.get_coro()}')
    for task in started_task:
        await task

asyncio.run(main())


# await on main task will result in exception. to avoid:
# Examples: Running from main()

# tasks = asyncio.all_tasks()
# current = asyncio.current_task()
# for task in tasks:
#     if task is current:
#         continue
#     await task

# OR

# tasks = asyncio.all_tasks()
# current = asyncio.current_task()
# tasks.remove(current)
# for task in tasks:
#     await task
