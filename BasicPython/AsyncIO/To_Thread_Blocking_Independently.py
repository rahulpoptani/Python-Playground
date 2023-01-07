
import time
import asyncio

def blocking_task():
    print('task is running')
    time.sleep(2)
    print('task is done')

async def main():
    coro = asyncio.to_thread(blocking_task)
    asyncio.create_task(coro)

asyncio.run(main())