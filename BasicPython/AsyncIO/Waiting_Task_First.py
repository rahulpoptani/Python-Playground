
from random import random
import asyncio

async def task_coro(arg):
    value = random()
    await asyncio.sleep(value)
    print(f'task {arg} done with: {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # only wait until first task complete and then return cursor back to main. Observe the output
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print('done')
    first = done.pop()
    print(first)

# The other tasks are not canceled and continue to run concurrently. Their execution is cut short because the asyncio program is terminated.

asyncio.run(main())

