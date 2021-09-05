
import logging
import Logging_Advanced

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('logs/basic.log')
file_handler.setFormatter(formatter)

# Stream the output to console as well
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter) # Create a new formatter or use the same one

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.exception will print the stack trace in log. It's Equivalent to logger.ERROR + Exception message
        logger.exception('Tried divide by Zero')
    else:
        return result

num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))