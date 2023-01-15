# loop until we have pending items

import asyncio
import aiohttp
from aiohttp import ClientSession
from Util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url,1)),
            asyncio.create_task(fetch_status(session, url,2))
            ]
        
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())