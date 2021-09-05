
import logging
# getting a new logger for this class, so that the import of this class does not create and merge same log file. 
# Ex: import Logging_Advanced will create a new logger employee.log and all the logs of the class importing this class will 
# also be combined in it as well as the name will be employee.log 
logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logs/employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1 = Employee('Corey', 'Schafer')
emp_1 = Employee('Jane', 'Doe')
