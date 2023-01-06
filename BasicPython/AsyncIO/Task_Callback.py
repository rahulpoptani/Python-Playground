# We can add a done callback function to a task via the add_done_callback() method.
# The add_done_callback() method can be used to add or register as many done callback functions as we like.
# We can also remove or de-register a callback function via the remove_done_callback() function.


# IMPORTANT: Always pass task object to callback
# TypeError: callback() takes 0 positional arguments but 1 was given

import asyncio

# 5. the done callback function is called by the event loop, reporting a message.
def callback(task):
    print('task is done')

async def task_coroutine():
    # 4. The task runs, reports a message, and sleeps for a moment before terminating normally.
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    # 1. The main() coroutine reports a message, then creates and schedules the task coroutine.
    task = asyncio.create_task(task_coroutine())
    # 2. It then adds the done callback function to the task to be executed when the task is finished.
    task.add_done_callback(callback)
    # 3. The main() coroutine then suspends and awaits the task to be completed.
    await task
    # 6. The main() coroutine resumes, reports its own final message and the program ends.
    print('main coroutine done')

asyncio.run(main())

