

import asyncio

async def task_coroutine():
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    # 1. The main() coroutine reports a message, then creates and schedules the task coroutine.
    task = asyncio.create_task(task_coroutine())
    # 2. The main() coroutine then cancels the task before it has had an opportunity to execute. 
    was_cancelled = task.cancel()
    print(f'was cancelled: {was_cancelled}')
    # 3. The main() coroutine then sleeps for a moment to allow the task to respond to the request to be canceled.
    await asyncio.sleep(0.1)
    print(f'cancelled: {task.cancelled()}')
    print('main couroutine done')

asyncio.run(main())