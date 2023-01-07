
import time
import asyncio

def blocking_task():
    print(f'task is running')
    time.sleep(2)
    print('task is done')
    return 100


# main coroutine
async def main():
    coro = asyncio.to_thread(blocking_task)
    result = await coro
    print(f'Got: {result}')

asyncio.run(main())