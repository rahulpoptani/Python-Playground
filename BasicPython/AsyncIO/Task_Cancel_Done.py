
import asyncio

async def task_coroutine():
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    await task
    was_cancelled = task.cancel()
    print(f'was cancelled: {was_cancelled}')
    await asyncio.sleep(0.1)
    print(f'cancelled: {task.cancelled()}')
    print('main couroutine done')

asyncio.run(main())