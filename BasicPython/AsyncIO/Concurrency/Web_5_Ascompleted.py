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
        fetchers = [fetch_status(session, 'https://example.com', 10),
                    fetch_status(session, 'https://example.com', 2),
                    fetch_status(session, 'https://example.com', 7)]
        
        # as_completed will wrap each coroutine as task and start running concurrently
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())