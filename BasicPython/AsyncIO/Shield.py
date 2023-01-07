# You can protect a task from being canceled by wrapping it in a call to asyncio.shield().
# It may be useful in asyncio programs where some tasks can be canceled, but others, perhaps with a higher priority cannot.

# Example:
    # define a simple coroutine task that takes an integer argument, sleeps for a second, then returns the argument. The coroutine can then be created and scheduled as a Task.
    # define a second coroutine that takes a task, sleeps for a fraction of a second, then cancels the provided task.
    # In the main coroutine, we can then shield the first task and pass it to the second task, then await the shielded task.
    # The expectation is 
        # the shield will be canceled and leave the inner task intact. 
        # The cancellation will disrupt the main coroutine. 
        # We can check the status of the inner task at the end of the program and we expect it to have been completed normally, regardless of the request to cancel made on the shield.


import asyncio

async def simple_task(number):
    await asyncio.sleep(1)
    return number

async def cancel_task(task):
    await asyncio.sleep(0.2)
    was_cancelled = task.cancel()
    print(f'cancelled: {was_cancelled}')

async def main():
    # create coroutine
    coro = simple_task(1)
    # create task
    task = asyncio.create_task(coro)
    # create a shield task
    shielded = asyncio.shield(task)
    # create task to cancel the previous task
    asyncio.create_task(cancel_task(shielded))
    try:
        result = await shielded
        print(f'got: {result}')
    except asyncio.CancelledError:
        print('shield was cancelled')
    await asyncio.sleep(1)
    # report details of task
    print(f'shielded: {shielded}')
    print(f'task: {task}')

asyncio.run(main())


