import asyncio

def callback(task):
    print('task is done')

async def task_coroutine():
    # 3. The task runs, reports a message, and sleeps for a moment. This gives the task time to start running
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    # 1. adds the done callback function to the task to be executed when the task is finished.
    task.add_done_callback(callback)
    # 2. suspends and awaits the task to be completed
    await asyncio.sleep(0.1)
    # 4. It then resumes and removes the done callback function from the running task.
    task.remove_done_callback(callback) # if the callbacl is not added at first place, then remove callback does nothing
    # 5. The main() coroutine then awaits the task to be completed
    await task
    print('main coroutine done')

asyncio.run(main())

print('===========================')

# adding a done callback after the task is done. 
# Before the asyncio event loop terminates, it executes the done callback function added to the task, reporting its message.

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    await task
    task.add_done_callback(callback)
    print('main coroutine done')

asyncio.run(main())