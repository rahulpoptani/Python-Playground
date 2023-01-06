import asyncio

async def task_coro(value):
    print(f'task {value} executing')
    await asyncio.sleep(1)
    return value * 10

async def main():
    print('Main running')
    values = await asyncio.gather(*[task_coro(_) for _ in range(1,10)])
    print(values)
    print('main done')

asyncio.run(main())

