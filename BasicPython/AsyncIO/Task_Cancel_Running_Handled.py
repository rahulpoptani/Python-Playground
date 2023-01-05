# If a coroutine wrapped in a task handles the CancelledError then the task will not be canceled, may continue to run, and will not be marked with the canceled status meaning the cancelled() method will return False.
# This means that although the cancel() method may return True indicating that the task will be canceled, it does not mean that that will be canceled, only that the task has the potential to be canceled.
 
import asyncio

async def task_coroutine():
    try:
        # 2. The task runs, reports a message and sleeps for a while.
        print('executing the task')
        await asyncio.sleep(1)
    except asyncio.CancelledError as e:
        print(f'Received a request to cancel with: {e}')

async def main():
    print('main coroutine started')
    task = asyncio.create_task(task_coroutine())
    # 1. suspends and awaits a moment to allow the task coroutine to begin running.
    await asyncio.sleep(0.1)
    # 3. The main() coroutine resumes and cancels the task. It reports that the request to cancel the task was successful.
    was_cancelled = task.cancel('Stop this task')
    print(f'was cancelled: {was_cancelled}')
    # 4. It then sleeps for a moment to allow the task to respond to the request to be canceled.
    await asyncio.sleep(0.1)
    print(f'cancelled: {task.cancelled()}')
    print('main couroutine done')

asyncio.run(main())