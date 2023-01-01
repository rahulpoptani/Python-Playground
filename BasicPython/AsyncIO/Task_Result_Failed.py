import asyncio

async def task_coroutine():
    print('executing task')
    await asyncio.sleep(1)
    raise Exception('something bad happened')
    return 99

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(1.1)
    try:
        # exception will be thrown once you get the result
        value = task.result()
        print(f'Result: {value}')
    except Exception as e:
        print(f'Failed with: {e}')
    print('main coroutine done')

asyncio.run(main())