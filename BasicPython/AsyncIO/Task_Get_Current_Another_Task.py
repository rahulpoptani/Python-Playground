
import asyncio

async def another_coroutine():
    print('executing the coroutine')
    task = asyncio.current_task()
    print(task)

async def main():
    print('Main couroutine started')
    task = asyncio.create_task(another_coroutine())
    await task
    print('Main coroutine done')

asyncio.run(main())