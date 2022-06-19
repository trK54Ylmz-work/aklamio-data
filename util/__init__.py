from .log import init_logging
from ini import ConfigParser

# initialize config
config = ConfigParser.load()

# initialize logger
logger = init_logging('app', file=False, stdout=True)
