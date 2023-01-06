# The asyncio.gather() module function allows the caller to group multiple awaitables together.
# Once grouped, the awaitables can be executed concurrently, awaited, and canceled.
# It is a helpful utility function for both grouping and executing multiple coroutines or multiple tasks.


# run a collection of awaitable
# result = await asyncio.gather(coro(), asyncio.create_task(coro2()))

# We may use the asyncio.gather() function in situations where we may create many tasks or coroutines up-front 
# and then wish to execute them all at once and wait for them all to complete before continuing on.
# This is a likely situation where the result is required from many like-tasks, e.g. same task or coroutine with different data.

# The gather() function is more powerful than simply waiting for tasks to complete.
# It allows a group of awaitables to be treated as a single awaitable.
# This allows:
    # Executing and waiting for all awaitables in the group to be done via an await expression.
    # Getting results from all grouped awaitables to be retrieved later via the result() method.
    # The group of awaitables to be canceled via the cancel() method.
    # Checking if all awaitables in the group are done via the done() method.
    # Executing callback functions only when all tasks in the group are done.
    # And more.


# The asyncio.gather() function takes one or more awaitables as arguments.
# Recall an awaitable may be a coroutine, a Future or a Task.
# Therefore, we can call the gather() function with:
    # Multiple tasks
    # Multiple coroutines
    # Mixture of tasks and coroutines

# If Task objects are provided to gather(), they will already be running because Tasks are scheduled as part of being created.

# gather() Returns a Future
# The gather() function does not block.
# Instead, it returns an asyncio.Future object that represents the group of awaitables.
# Once the Future object is created it is scheduled automatically within the event loop.
# The awaitable represents the group, and all awaitables in the group will execute as soon as they are able.
# This means that if the caller did nothing else, the scheduled group of awaitables will run 
# It also means that you do not have to await the Future that is returned from gather().

# Awaiting gather()’s Future
# =============================
# The returned Future object can be awaited which will wait for all awaitables in the group to be done

# The gather() function takes awaitables and itself returns an awaitable.
# Therefore, we can create nested groups of awaitables.
# Example:
# group1 = asyncio.gather(coro1(), coro2())
# group2 = asyncio.gather(group1, coro3())
# await group2


# The “return_exceptions” argument to gather() can be set to True which will catch exceptions and provide them as return values instead of re-raising them in the caller.
# result = await asyncio.gather(coro(), asyncio.create_task(coro2()), return_exceptions=True)

# Check if group is done: group.done()
# cancel group: group.cancel()

import asyncio

async def task_coro(value):
    print(f'task {value} executing')
    await asyncio.sleep(1)

async def main():
    print('Main running')
    await asyncio.gather(*[task_coro(_) for _ in range(1,10)])
    print('main done')

asyncio.run(main())

