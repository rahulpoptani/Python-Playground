
import asyncio

async def main():
    print('Main couroutine started')
    task = asyncio.current_task()
    print(task)

asyncio.run(main())