import asyncio
from Util import delay

async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")
 
 
async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    # if we don't await then main corutine will finish first and final result will not be able to come back from couroutine
    await first_delay
    await second_delay

asyncio.run(main())