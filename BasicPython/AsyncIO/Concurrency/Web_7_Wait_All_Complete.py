# wait for all tasks to complete

import asyncio
import aiohttp
import logging
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
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'python://example.com'))
            ]
        done, pending = await asyncio.wait(fetchers) # pending will always be 0, as "wait" won't return until all is completed

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            # result = await done_task # we'll get exception here, if any
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Request got an exception', exc_info=done_task.exception())

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())