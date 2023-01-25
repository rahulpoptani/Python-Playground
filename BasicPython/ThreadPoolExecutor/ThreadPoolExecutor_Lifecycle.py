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

# When to Use ThreadPoolExecutor
    # Use the ThreadPoolExecutor class when you need to execute many short- to modest-length tasks throughout the duration of your application.
    # Use the ThreadPoolExecutor class when you need to execute tasks that may or may not take arguments and may or may not return a result once the tasks are complete.
    # Use the ThreadPoolExecutor class when you need to execute different types of ad hoc tasks, such as calling different target task functions.
    # Use the ThreadPoolExecutor class when the types of tasks of and timing of when you need to execute tasks varies at runtime.
    # Use the ThreadPoolExecutor class when you need to be able to queue up a large number of tasks.
    # Use the ThreadPoolExecutor class when you need to be able to check on the status of tasks during their execution.
    # Use the ThreadPoolExecutor class when you need to take action based on the results of tasks, such as the first task to complete, the first task to raise an exception, or results as they become available.

# When to Use Thread
    # Use the Thread class when you have a single one-off task to execute via the target argument.
    # Use the Thread class for many similar tasks with different arguments that do not return a result, such as via the “target” argument or by multiple instances of a customized Thread class.
    # Use the Thread class when you have a lot of complex behavior spread across multiple functions and/or when you have a lot of state to be managed. In these cases, you can extend the Thread class and define your instance variables and task functions.
    # Use the Thread class for long-running tasks by extending the Thread class and treat the object as a service within your application


# Don’t Use Thread When…
    # Don’t use the Thread class for many different task types, e.g. different target functions. You are better off using the ThreadPoolExecutor.
    # Don’t use the Thread class when you require a result from tasks; you could achieve this by extending the Thread class, although it’s easier with the ThreadPoolExecutor.
    # Don’t use the Thread class when you need to execute and manage multiple tasks concurrently. This could be achieved with Thread but would require developing the tools and infrastructure.
    # Don’t use the Thread class when you are required to check on the status of tasks while they are executing; this can be achieved with Future objects returned when submitting tasks to the ThreadPoolExecutor.

