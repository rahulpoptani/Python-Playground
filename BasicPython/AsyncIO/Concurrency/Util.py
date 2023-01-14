import asyncio
import functools
import time
from typing import Callable, Any


async def delay(seconds: int) -> int:
    print(f'sleeping for {seconds} seconds')
    await asyncio.sleep(seconds)
    print(f'finished sleeping for {seconds} seconds')
    return seconds

 
def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'starting {func} with args {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'finished {func} in {total:.4f} second(s)')
 
        return wrapped
 
    return wrapper

