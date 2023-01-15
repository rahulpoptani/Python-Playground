import asyncio
import logging
from aiohttp import ClientSession
from Util import async_timed

# Return as soon as hit first exception, done list will have failed task along with success task if any
# Pending list will have pending tasks

@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com', 3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', 3))
            ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Request got an exception', exc_info=done_task.exception())
        
        for pending_task in pending:
            print(f'Cancelled task: {pending_task}')
            pending_task.cancel()

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

# The benefit of this approach is we can fail fast as soon as any task in failed