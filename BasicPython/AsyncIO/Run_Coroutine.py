import asyncio

# define custom coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1)

# main coroutine
async def main():
    # execute custom coroutine
    await custom_coro()

# start coroutine program - create event loop using asyncio.run()
asyncio.run(main())
