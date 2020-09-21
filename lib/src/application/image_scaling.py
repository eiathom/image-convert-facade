from typing import List

from lib.src.domain.image_resizer import (
    ConvertCommand,
    MagickProgram,
    Program,
    ResizeOption,
)
from lib.src.util.logger import get_logger
from lib.src.util.io import load_json_data_from_file


logger = get_logger(__name__)


def jpeg_scaler_handler(args: dict) -> List[Program]:
    if 'datafile' not in args:
        logger.info('jpeg image scaler handler v1')
        return [_jpeg_scaler_v1_handler(
            input_filepath=args.get('input_filepath'),
            output_filename=args.get('output_filename'),
            scale=args.get('scale')
        )]
    logger.info('jpeg image scaler handler v2')
    return _jpeg_scaler_v2_handler(datafile=args.get('datafile'))


def _build_resize_program(
    input_filepath: str,
    output_filename: str,
    scale: int
    ) -> Program:
    if all([input_filepath, output_filename, scale]):
        logger.info('building resize Magick program')
        resizeOption = ResizeOption(scale_width=scale, scale_height=scale)
        convertCommand = ConvertCommand(
            input_filepath=input_filepath,
            output_filename=output_filename,
            options=[resizeOption]
        )
        return MagickProgram(command=convertCommand)

    logger.info('not enough arguments passed')


def _jpeg_scaler_v1_handler(
    input_filepath: str,
    output_filename: str,
    scale: int
    ) -> Program:
    return _build_resize_program(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale=scale
    )


def _jpeg_scaler_v2_handler(datafile: str) -> List[Program]:
    try:
        json_data = load_json_data_from_file(datafile)
        return [_jpeg_scaler_v1_handler(**obj) for obj in json_data['data']]
    except FileNotFoundError as exception:
        logger.info(f'json data file not found: {str(exception)}')
