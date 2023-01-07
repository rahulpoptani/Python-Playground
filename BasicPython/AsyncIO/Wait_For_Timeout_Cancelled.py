
from random import random
import asyncio

async def task_coro(arg):
    value = 1 + random()
    print(f'task got {value}')
    await asyncio.sleep(value)
    print('task done')

async def task_cancel(other_task):
    await asyncio.sleep(0.3)
    other_task.cancel()

async def main():
    task = asyncio.create_task(task_coro(1))
    wait_coro = asyncio.wait_for(task, timeout=1)
    asyncio.create_task(task_cancel(task))
    try:
        await wait_coro
    except asyncio.TimeoutError:
        print('Gave up waiting, task cancelled')
    except asyncio.CancelledError:
        print('Task was cancelled externally')
        print(task)

asyncio.run(main())
