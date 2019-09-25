import logging
from logging.handlers import TimedRotatingFileHandler


handler = TimedRotatingFileHandler('server_log_config', when='midnight', backupCount=10)
logger = logging.getLogger('app.main')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

fh = logging.FileHandler('app.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
