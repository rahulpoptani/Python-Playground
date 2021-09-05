def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

hi_func()
bye_func()


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

