# Reference
# https://docs.python.org/3/library/logging.html
# https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

import logging


# Setup logging to console and write a couple things
# Create a logger object to use, name doesn't really matter I don't think
log = logging.getLogger('deezlogs')
# Set minimum level to include (see ref link for options)
log.setLevel(logging.INFO)
# Set log format
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add a console output handler also at INFO level
log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(logging.INFO)
log_console_handler.setFormatter(log_formatter)
log.addHandler(log_console_handler)
# Add a file output handler also at INFO level
# Different handlers can have different log levels and formats but I personally would probably not change this
# other than using debug sometimes for deep troubleshooting
log_file_handler = logging.FileHandler(filename='deezlogs.log')
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(log_formatter)
log.addHandler(log_file_handler)

# NOTE logging.basicConfig() can also be used which does the same things but may be a few less lines
# This code needs testing, it was pulled from stackoverflow as is:
#log_file_handler = logging.FileHandler(filename='deezlogs.log')
#log_console_handler = logging.StreamHandler()
#log_handlers = [log_file_handler, log_console_handler]
#
#logging.basicConfig(
#    level=logging.INFO,
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#    handlers=log_handlers
#    )
#
#log = logging.getLogger('deezlogs')



# Now write something!
log.debug('This is a debug level message, you probably don\'t care until you do')
log.info('This is an info level message, no biggie')
log.warning('This is a warning level message, be careful out there')
log.error('This is an error level message, please help!')
log.critical('This is a critical level message, you\'re hair is currently on fire sir')
