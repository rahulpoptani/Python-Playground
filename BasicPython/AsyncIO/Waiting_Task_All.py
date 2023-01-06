# The asyncio.wait() function can be used to wait for a collection of asyncio tasks to complete.
# the asyncio.wait() is a coroutine function that returns a coroutine.

# The call to wait can be configured to wait for different conditions, such as 
    # all tasks being completed
    # the first task completed 
    # the first task failing with an error.

# The asyncio.wait() will not return until some condition on the collection of tasks is met.

# The wait() function returns a tuple of two sets. 
    # The first set contains all task objects that meet the condition
    # the second contains all other task objects that do not yet meet the condition.

# Example:
# done, pending = await asyncio.wait(tasks)

# wait all task to complete
# done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

# wait for First tsask to complete
# done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

# wait for first to fail
# done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

# wait until timeout
# done, pending = await asyncio.wait(tasks, timeout=3)


from random import random
import asyncio

async def task_coro(arg):
    value = random()
    await asyncio.sleep(value)
    print(f'task {arg} done with: {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all task to complete
    done, pending = await asyncio.wait(tasks)
    print('all done')

asyncio.run(main())