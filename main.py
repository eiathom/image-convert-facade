import logging

from lib.src.presentation.cli import (
    image_convert_facade_parser,
    image_scaler,
)


logger = logging.getLogger(__name__)


CLI_VERSION = 'v2'


if __name__ == '__main__':
    logger.info('starting CLI...')

    args = image_convert_facade_parser.parse_args()
    args_dict = vars(args)

    logger.info(f'cli_version:{CLI_VERSION}, args={args_dict}')

    image_scaler(CLI_VERSION, args_dict)
