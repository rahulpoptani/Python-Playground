import asyncio, signal
from asyncio import AbstractEventLoop, CancelledError
from typing import Set
from Util import delay

# callback when KeyboardInterrup Exception is raised
def cancel_task():
    print('Got SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} tasks')
    [task.cancel() for task in tasks]

async def main():
    # get event loop and add signal handler
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_task)
    try:
        await delay(10) # raised CancelledError, hence catch exception
    except CancelledError:
        print('Task Cancelled')

asyncio.run(main())