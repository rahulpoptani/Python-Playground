import asyncio

async def task_coro(value):
    print(f'task {value} executing')
    await asyncio.sleep(1)

async def main():
    print('Main running')
    group1 = asyncio.gather(task_coro(0), task_coro(1), task_coro(2))
    group2 = asyncio.gather(task_coro(3), task_coro(4), task_coro(5))
    group3 = asyncio.gather(group1, group2)
    await group3 
    print('main done')

asyncio.run(main())

