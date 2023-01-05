# If the task is already done, it cannot be canceled and the cancel() method will return False and the task will not have the status of canceled.
# The next time the task is given an opportunity to run, it will raise a CancelledError exception.
# If the CancelledError exception is not handled within the wrapped coroutine, the task will be canceled.
# Otherwise, if the CancelledError exception is handled within the wrapped coroutine, the task will not be canceled.

import asyncio

async def task_coroutine():
    # 2. The task runs, reports a message and sleeps for a while.
    print('executing the task')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    # 1. suspends and awaits a moment to allow the task coroutine to begin running.
    await asyncio.sleep(0.1)
    # 3. The main() coroutine resumes and cancels the task. It reports that the request to cancel the task was successful.
    was_cancelled = task.cancel()
    print(f'was cancelled: {was_cancelled}')
    # 4. It then sleeps for a moment to allow the task to respond to the request to be canceled.
    await asyncio.sleep(0.1)
    print(f'cancelled: {task.cancelled()}')
    print('main couroutine done')

asyncio.run(main())