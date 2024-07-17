import logging

# Create and configure logger
logging.basicConfig(
     filename='c:/temp/bm.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )
# Creating an object
logger = logging.getLogger()
