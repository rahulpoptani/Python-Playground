
from random import random
import asyncio

async def task_coro(arg):
    value = random()
    await asyncio.sleep(value)
    print(f'task {arg} done with: {value}')
    if value < 0.5:
        raise Exception(f'Something bad with args: {arg}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for first task to fail or all task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print('done')
    first = done.pop()
    print(first)


asyncio.run(main())

