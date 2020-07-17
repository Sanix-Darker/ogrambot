import logging

# Create a custom logger
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
# Create handlers
f_handler = logging.FileHandler('logs.log')
# Create formatters and add it to handlers
f_format = logging.Formatter(' %(asctime)s > %(process)d-%(levelname)s-%(message)s')
f_handler.setFormatter(f_format)
# Add handlers to the logger
logger.addHandler(f_handler)
