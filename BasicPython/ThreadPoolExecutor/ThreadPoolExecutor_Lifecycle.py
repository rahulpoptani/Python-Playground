# ThreadPoolExecutor Lifecycle
# 1. Create - Create thread pool by calling constructor ThreadPoolExecutor()
# 2. Submit - Submit task and get future via map or submit method
# 3. Wait - Wait and get result as task completed via wait or as_completed method
# 4. Shutdown - Shutdown the thread pool

# 1. Create:
# When intsance of thread pool is created it must be be configured with fixed number of threads
# Default = Total CPU + 4

# 2. Submit:
# Submit task for asynchronous execution
# Map
    # map method assume the target function takes exactly one argument, which is one item per iterable.
    # More than one argument? - bundle argument to have list or dict structure or use submit method
    # No argument? - map cannot be used. use Submit method
# Submit
    # Submit returns future immediately

# 3. Wait:
# wait() - wait for one or more future objects until they are completed
# as_completed() - return future objects from a collection as they completed their execution

# 4. Shutdown:
# Close down the thread pool

# Thread Pool using Context Manager - Preferred Way

# Not suited for background task

# When to use ThreadPoolExecutor
    # Your tasks can be defined by a pure function that has no state or side effects.
    # Your task can fit within a single Python function, likely making it simple and easy to understand.
    # You need to perform the same task many times, e.g. homogeneous tasks.
    # You need to apply the same function to each object in a collection in a for-loop.

# When to use multiple ThreadPoolExecutor
    # You need to perform groups of different types of tasks; one thread pool could be used for each task type.
    # You need to perform a pipeline of tasks or operations; one thread pool can be used for each step


# Don’t Use ThreadPoolExecutor When…
    # You have a single task; consider using the Thread class with the target argument.
    # You have long-running tasks, such as monitoring or scheduling; consider extending the Thread class.
    # Your task functions require state; consider extending the Thread class.
    # Your tasks require coordination; consider using a Thread and patterns like a Barrier or Semaphore.
    # Your tasks require synchronization; consider using a Thread and Locks.
    # You require a thread trigger on an event; consider using the Thread class.

