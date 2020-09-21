import argparse

image_convert_facade_parser = argparse.ArgumentParser(
    description='manipulate image files',
    epilog='end',
)

subparsers = image_convert_facade_parser.add_subparsers(
    title='subcommands',
    description='valid subcommands',
    help='additional help'
)

jpeg_scaler_command = subparsers.add_parser('jpeg_scaler', aliases=['jps'])

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
