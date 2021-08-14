import logging
import time
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger('Rotating Log')
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('LogRotationExample.log', when='s', interval=5)
logger.addHandler(handler)    

for i in range(100):
    logger.info("This is a test!")
    time.sleep(5)

