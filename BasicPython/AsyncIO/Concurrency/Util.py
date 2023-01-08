import asyncio

async def delay(seconds: int) -> int:
    print(f'sleeping for {seconds} seconds')
    await asyncio.sleep(seconds)
    print(f'finished sleeping for {seconds} seconds')
    return seconds