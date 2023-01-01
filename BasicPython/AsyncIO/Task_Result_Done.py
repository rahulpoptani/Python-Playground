import asyncio

async def task_coroutine():
    print('executing task')
    await asyncio.sleep(1)
    return 99

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    await task
    value = task.result()
    print(f'Result: {value}')
    print('main coroutine done')

asyncio.run(main())