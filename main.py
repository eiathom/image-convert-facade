from lib.src.application.image_scaling import jpeg_scaler_handler
from lib.src.infrastructure.image_io import run_command
from lib.src.presentation.cli import image_convert_facade_parser
from lib.src.util.logger import get_logger


logger = get_logger(__name__)


if __name__ == '__main__':
    logger.info('starting CLI...')

    args = image_convert_facade_parser.parse_args()
    args_dict = vars(args)

    logger.info(f'args={args_dict}')

    programs = jpeg_scaler_handler(args_dict)

    if programs:
        for program in programs and programs:
            run_command(program=program)

