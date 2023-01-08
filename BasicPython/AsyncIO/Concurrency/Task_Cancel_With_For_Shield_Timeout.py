# Keep coroutine running and inform that the timeout is exceeded and do not cancel

import asyncio
from Util import delay
 
async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Task took longer than 5 seconds, it will finish soon')
        result = await task
        print(result)

asyncio.run(main())