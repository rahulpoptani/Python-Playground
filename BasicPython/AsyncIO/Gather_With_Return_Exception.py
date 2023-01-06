import asyncio

async def task_coro(value):
    print(f'task {value} executing')
    await asyncio.sleep(1)
    if value == 0:
        raise Exception('Something bad happen')
    return value * 10

async def main():
    print('Main running')
    values = await asyncio.gather(*[task_coro(_) for _ in range(10)], return_exceptions=True)
    print(values)
    print('main done')

asyncio.run(main())

