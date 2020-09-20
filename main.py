import os

from lib.src.presentation.cli import (
    image_convert_facade_parser,
    image_scaler,
)
from lib.src.util.logger import get_logger


logger = get_logger(__name__)


if __name__ == '__main__':
    logger.info('starting CLI...')

    args = image_convert_facade_parser.parse_args()
    args_dict = vars(args)

    logger.info(f'args={args_dict}')

    image_scaler(args_dict)
