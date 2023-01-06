
import asyncio

async def another_coroutine():
    print('executing the coroutine')
    task = asyncio.current_task()
    print(task)

async def main():
    print('Main couroutine started')
    await another_coroutine()
    print('Main coroutine done')

asyncio.run(main())