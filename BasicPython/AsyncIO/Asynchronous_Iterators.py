# You can create and use asynchronous iterators in asyncio programs by defining an object that implements the 
    # __aiter__() 
    # __anext__()

# The __aiter__() method must return an instance of the iterator.
# The __anext__() method must return an awaitable that steps the iterator

import asyncio

class AsyncIterator():
    def __init__(self):
        self.counter = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(0.2)
        return self.counter

async def main():
    async for item in AsyncIterator():
        print(item)

asyncio.run(main())
