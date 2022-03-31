import logging

file_logger = logging.getLogger(__name__)
file_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='crawl.log')
file_handler.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.ERROR)

file_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s] : %(message)s")
file_handler.formatter = file_formatter
c_handler.formatter = file_formatter
file_logger.addHandler(file_handler)
file_logger.addHandler(c_handler)

file_logger.debug('MSG')
file_logger.info('MSG')
file_logger.warning('MSG')
file_logger.error('MSG')
file_logger.critical('MSG')
