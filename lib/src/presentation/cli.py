import argparse
import json
import logging
import os
import sys
from pathlib import Path

from lib.src.application.image_scaling import scale_image


logger = logging.getLogger(__name__)


image_convert_facade_parser = argparse.ArgumentParser(
    prog='image_convert_facade',
    usage='%(prog)s [options]',
    description='manipulate image files',
    epilog='end',
)

subparsers = image_convert_facade_parser.add_subparsers(
    title='subcommands',
    description='valid subcommands',
    help='additional help'
)

jpeg_scaler_command = subparsers.add_parser('jpeg_scaler_v1', aliases=['jps1'])

jpeg_scaler_command.add_argument(
    '-i',
    '--input_filepath',
    action='store',
    metavar='INPUT_FILEPATH',
    type=str,
    dest='input_filepath',
    help='the path to the image file to scale'
)

jpeg_scaler_command.add_argument(
    '-o',
    '--output_filename',
    action='store',
    metavar='OUTPUT_FILENAME',
    type=str,
    dest='output_filename',
    help='the name of the newly scaled image'
)

jpeg_scaler_command.add_argument(
    '-s',
    '--scale',
    action='store',
    metavar='SCALE',
    type=int,
    dest='scale',
    default=100,
    help='the value to scale the input image by'
)

jpeg_scaler_v2_command = subparsers.add_parser('jpeg_scaler_v2', aliases=['jps2'])

jpeg_scaler_v2_command.add_argument(
    '-d',
    '--datafile',
    action='store',
    metavar='DATAFILE',
    type=str,
    dest='datafile',
    help='datafile containing multiple data to scale images'
)


def image_scaler(version: str, args: dict) -> None:
    if version == 'v1':
        jpeg_scaler_v1(
            input_filepath=args.get('input_filepath'),
            output_filename=args.get('output_filename'),
            scale=args.get('scale')
        )
    else:
        jpeg_scaler_v2(datafile=args.get('datafile'))


def jpeg_scaler_v1(input_filepath: str, output_filename: str, scale: int) -> None:
    if all([input_filepath, output_filename, scale]):
        scale_image(
            input_filepath=input_filepath,
            output_filename=output_filename,
            scale=scale
        )
    else:
        logger.info('not enough arguments passed')
        logger.info(
            f'input_filepath={input_filepath}',
            f'output_filename={output_filename}',
            f'scale={scale}'
        )


def jpeg_scaler_v2(datafile: str) -> None:
    if datafile and Path(datafile).exists():
        with open(datafile) as json_file:
            data = json.load(json_file)
            for d in data['data']:
                jpeg_scaler_v1(**d)
    else:
        logger.info('data file not found')
        logger.info(f'datafile={datafile}')
