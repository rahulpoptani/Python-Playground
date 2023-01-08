# A context manager is a Python construct that provides a try-finally like environment with a consistent interface and handy syntax
# An asynchronous context manager is a Python object that implements the __aenter__() and __aexit__() methods.

import asyncio

class CustomContextManager:
    async def __aenter__(self):
        print('entering context manager')
        await asyncio.sleep(0.5)  
    async def __aexit__(self, exc_type, exc, tb):
        print('exiting context manager')
        await asyncio.sleep(0.5)

async def custom_coroutine():
    print('before context manager')
    async with CustomContextManager() as manager:
        print('within context manager')
    print('after context manager')


asyncio.run(custom_coroutine())