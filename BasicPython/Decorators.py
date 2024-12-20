

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

@timing_decorator
def data_preprocessing(data):
    # Some heavy computation here
    processed = [x*2 for x in data]
    return processed

# Using the decorated function
data = [1, 2, 3, 4]
processed = data_preprocessing(data)


##########################################################

def decorator_func(original_func):
    def wrapped_func():
        print('Called before {}'.format(original_func.__name__))
        return original_func()
    return wrapped_func

@decorator_func
def display():
    print('Display Function Ran')

display()

##########################################################

def decorator_func(original_func):
    def wrapped_func(*args, **kwargs):
        print('Called before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapped_func

@decorator_func
def display(name, age):
    print('Display Function Ran with {name} {age}'.format(name=name, age=age))

display(name='Rahul', age=31)

##########################################################

class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func
    def __call__(self, *args, **kwargs):
        print('Called before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)

@decorator_class
def display(name, age):
    print('Display Function Ran with {name} {age}'.format(name=name, age=age))

display(name='Rahul', age=31)

