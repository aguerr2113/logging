import logging

logging.basicConfig(
    level=logging.INFO, 
    filename = "log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s")

# Logging a value of a variable
x = 2

logging.info(f"the value of x is {x}")

# log a stack trace
try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError",exc_info=True)

# customer loggers
logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)


logger.info('test the customer logger')


# Levels of importanceo top to bottom
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
