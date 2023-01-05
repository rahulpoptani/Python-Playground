# how to check for and get an exception from a successfully done task.

import asyncio

async def task_coroutine():
    print('execuiting the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    await task
    ex = task.exception()
    print(f'Exception: {ex}')
    print('main coroutine done')

asyncio.run(main())