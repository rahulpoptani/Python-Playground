# pip install -Iv aiohttp==3.8.1

import asyncio
import aiohttp
from aiohttp import ClientSession
from Util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    # by default ClientSession creates 100 connections
    async with aiohttp.ClientSession() as session:
        url = 'https://google.com'
        status = await fetch_status(session, url)
        print(f'Status for {url} was {status}')

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
