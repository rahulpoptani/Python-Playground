# We can run blocking calls asynchronously in an asyncio program via the asyncio.to_thread() and loop.run_in_executor() functions.

# we often need to execute a blocking function call within an asyncio application.
# This could be for many reasons, such as:
    # To execute a CPU-bound task like calculating something.
    # To execute a blocking IO-bound task like reading or writing from a file.
    # To call into a third-party library that does not support asyncio yet.

# The task will not begin executing until the returned coroutine is given an opportunity to run in the event loop.
# The asyncio.to_thread() function creates a ThreadPoolExecutor behind the scenes to execute blocking calls.

# An alternative approach is to use the loop.run_in_executor() function.

import time
import asyncio

# blocking function
def blocking_task(value1, value2):
    print(f'task is running with {value1} and {value2}')
    time.sleep(2)
    print('task is done')

# background coroutine
async def background():
    while True:
        print('background task running')
        await asyncio.sleep(0.5)

# main coroutine
async def main():
    # run background task
    _ = asyncio.create_task(background())
    # create a coroutine for the blocking function call
    coro = asyncio.to_thread(blocking_task, 100, 'TEST')
    # execute call in new thread and await the result
    await coro

asyncio.run(main())