import asyncio
import aiohttp
from aiohttp import ClientSession
from Util import async_timed

# @async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://google.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        # gather will wrap coroutines in task and execute all at once
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
