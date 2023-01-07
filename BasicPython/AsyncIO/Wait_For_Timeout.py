
from random import random
import asyncio

async def task_coro(arg):
    value = random()
    print(f'task got {value}')
    await asyncio.sleep(value)
    print('task done')

async def main():
    task = task_coro(1)
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print('Gave up waiting, task cancelled')

asyncio.run(main())
