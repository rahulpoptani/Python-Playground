
from random import random
import asyncio

async def task_coro(arg):
    value = random() * 10
    await asyncio.sleep(value)
    print(f'task {arg} done with: {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all task to complete
    done, pending = await asyncio.wait(tasks, timeout = 3)
    print(f'Done: {len(done)} tasks compelted in time')

asyncio.run(main())