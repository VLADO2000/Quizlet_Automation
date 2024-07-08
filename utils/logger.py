import logging
import sys


def setup_logger(level=logging.INFO):
    """
    Setup logging function ensures consistent
    logging output throughout the project
    """
    logger.setLevel(level)
    handler = logging.FileHandler(filename='quizlet_automation.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = logging.getLogger(__name__)
setup_logger()
