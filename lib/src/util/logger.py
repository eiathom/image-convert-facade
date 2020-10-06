import logging
import os

from config import LOGGING


LOGGING_FORMAT = logging.Formatter(LOGGING.log_format)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOGGING.log_output_filepath)

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.WARNING)

console_handler.setFormatter(LOGGING_FORMAT)
file_handler.setFormatter(LOGGING_FORMAT)


def get_logger(logger_name: str) -> logging.Logger:
    """get a logger for given `logger_name`

    Args:
        logger_name (str): the name of this logger

    Returns:
        logging.Logger: a logger object
    """

    logger = logging.getLogger(name=logger_name)

    logger.setLevel(LOGGING.log_level)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
