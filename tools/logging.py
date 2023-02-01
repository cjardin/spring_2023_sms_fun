import logging
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) #SET INFO, or ERROR for prod
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s %(funcName)s():%(lineno)i: - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

