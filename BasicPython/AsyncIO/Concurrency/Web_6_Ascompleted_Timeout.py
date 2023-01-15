import asyncio
import aiohttp
from aiohttp import ClientSession
from Util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 5),
                    fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 4)]
        
        for finished_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('We got a timeout error!')
        
        for task in asyncio.tasks.all_tasks():
            print(task)

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

# Drawbacks:
    # 1. We don't know which coroutine we're waiting as order is nondeterministic
    # 2. Even after Timeout Exception is thrown the task as still running in background and with no control on task, it not easy to cancel the task if required