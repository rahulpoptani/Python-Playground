
import asyncio

def callback1(task):
    print('task is done')

def callback2(task):
    print(f'task: {task}')

async def task_coroutine():
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine(), name="MyTask")
    task.add_done_callback(callback1)
    task.add_done_callback(callback2)
    await task
    print('main coroutine done')

asyncio.run(main())

