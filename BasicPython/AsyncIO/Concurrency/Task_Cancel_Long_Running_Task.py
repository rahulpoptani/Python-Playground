import asyncio
from asyncio import CancelledError
from Util import delay

async def main():
    long_task = asyncio.create_task(delay(10))

    second_elaspsed = 0

    while not long_task.done():
        print('Task not finished, checking again in 1 second')
        await asyncio.sleep(1)
        second_elaspsed += 1
        if second_elaspsed == 5:
            long_task.cancel()
    
    try:
        await long_task # Exception CancelledError can only be thrown from await statement
    except CancelledError:
        print('Our task was cancelled')

asyncio.run(main())