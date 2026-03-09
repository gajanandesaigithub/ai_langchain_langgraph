from logger import logging

def add(a,b):
    logging.debug("Inside add() method")
    return a+b

logging.debug("before calling add() method")
add(10,15)
logging.debug("after calling add() method")