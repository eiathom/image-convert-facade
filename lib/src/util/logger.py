import logging
import os


logging.basicConfig(
    format="[%(levelname)s] %(asctime)s - %(message)s", level=logging.INFO
)


def get_logger(logger_name: str) -> logging.Logger:
    return logging.getLogger(logger_name)
