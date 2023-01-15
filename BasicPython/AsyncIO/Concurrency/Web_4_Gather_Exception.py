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
        urls = ['https://amazon.in/', 'abc://amazon.in']
        requests = [fetch_status(session, url) for url in urls]
        # return exception as string output and not exception type
        status_codes = await asyncio.gather(*requests, return_exceptions=True)
        
        exceptions = [res for res in status_codes if isinstance(res, Exception)]
        success_result = [res for res in status_codes if not isinstance(res, Exception)]

        print(f'All Results: {status_codes}')
        print(f'Finished Successfully: {success_result}')
        print(f'Threw Exceptions: {exceptions}')

# windows only
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

# catch: One request might complete in 1 second and another can take 20 seconds, we have to wait for 20 seconds to process the result of request which complete in 1 second.
# We should use "as_completed" to deal with this issue
