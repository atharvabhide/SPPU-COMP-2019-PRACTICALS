import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='basic_logger.log',
    filemode='w'
)

logging.debug("Debug message")

logging.info("Informative message")

logging.error("Error message")
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s- %(message)s',
    filename='basic_logger.log',
    filemode='a'
)

logging.debug('This is a log message.')
LogWithLevelName = logging.getLogger('myLoggerSample')
level = logging.getLevelName('INFO')
LogWithLevelName.setLevel(level)