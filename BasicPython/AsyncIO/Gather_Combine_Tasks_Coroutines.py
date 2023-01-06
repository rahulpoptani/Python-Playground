# Like a coroutine, an asyncio.Task is an awaitable.
# The coroutines provided to gather() will be wrapped in Task objects and scheduled for execution.
# The Task objects will already be scheduled for execution.

# means that some awaitables provided to a call to gather() could already be done. Awaiting the group only waits for those awaitables that are not already done.

# Notice: Task will be done first (as they are scheduled at time of creation) before coroutine

import asyncio

async def task_coro(value):
    print(f'task {value} running')
    await asyncio.sleep(1)

async def main():
    print('main starting')
    awaitables = [task_coro(0),
                asyncio.create_task(task_coro(1)),
                task_coro(2),
                asyncio.create_task(task_coro(3)),
                task_coro(4),
                asyncio.create_task(task_coro(5))]
    asyncio.gather(*awaitables)
    await asyncio.sleep(2)
    print('main done')

asyncio.run(main())