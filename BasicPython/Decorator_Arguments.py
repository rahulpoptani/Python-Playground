
# def decorator_function(original_function):
    
#     def wrapper_function(*args, **kwargs):
#         print('Executed Before', original_function.__name__)
#         original_function(*args, **kwargs)
#         print('Executed After', original_function.__name__, '\n')
    
#     return wrapper_function


# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('John', 25)
# display_info('Travis', 30)


#####################################################################################################################

# Nesting one more level and adding prefix


def prefix_decorator(prefix):
    def decorator_function(original_function):
        
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
        return wrapper_function
    
    return decorator_function


@prefix_decorator('TESTING')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)