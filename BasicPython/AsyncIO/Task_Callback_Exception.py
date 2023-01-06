# Out of two callbacks, one will raise exception and other will execute normally

import asyncio

def callback1(task):
    print('Callback1: task is done')
    raise Exception('Callback1: Something Bad Happened')

def callback2(task):
    print(f'Callback2: Task: {task}')

async def task_coroutine():
    print('Executing the task')
    await asyncio.sleep(1)

async def main():
    print('Main coroutine started')
    task = asyncio.create_task(task_coroutine())
    task.add_done_callback(callback1)
    task.add_done_callback(callback2)
    await task
    print('Main coroutine done')

asyncio.run(main())