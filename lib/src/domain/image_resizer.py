from typing import Optional

from lib.src.infrastructure.image_io import (
    does_file_exist,
    get_image_file_format,
    get_filetype,
    get_filepath_parents,
    merge_path_and_filename,
    run_command,
)

PERCENT_OPERATOR = 'PERCENT'

OPERATORS={
    PERCENT_OPERATOR: '%'
}

MAGICK_PROGRAM_NAME = 'magick'
MAGICK_CONVERT_COMMAND_NAME = 'convert'


def do_convert_image(
    input_filepath: str,
    output_filename: str,
    output_file_format: str
    ):
    command_args = get_command_args(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale_width=100,
        scale_height=100,
        operator=OPERATORS.get(PERCENT_OPERATOR),
        output_file_format=output_file_format
    )
    return run_command(
        program=MAGICK_PROGRAM_NAME,
        command=MAGICK_CONVERT_COMMAND_NAME,
        command_args=command_args,
    )


def do_scale_image(
    input_filepath: str,
    output_filename: str,
    scale: int
    ):
    command_args = get_command_args(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale_width=scale,
        scale_height=scale,
        operator=OPERATORS.get(PERCENT_OPERATOR)
    )
    return run_command(
        program=MAGICK_PROGRAM_NAME,
        command=MAGICK_CONVERT_COMMAND_NAME,
        command_args=command_args,
    )


def get_input_filepath_format(filepath):

    input_filepath_format = get_image_file_format(filepath)

    if not input_filepath_format:
        raise Exception(f'{filepath} is not an image')

    input_filepath_filetype = get_filetype(filepath)

    if input_filepath_format == 'jpeg' and input_filepath_filetype == 'jpg':
        input_filepath_format = input_filepath_filetype

    return input_filepath_format


def get_command_args(
    input_filepath: str,
    output_filename: str,
    scale_width: int,
    scale_height: int,
    operator: str,
    output_file_format: Optional[str] = None
    ) -> list:

    if not does_file_exist(input_filepath):
        raise Exception(f'{input_filepath} does not exist')

    if scale_width < 0 or scale_height < 0:
        raise Exception('width and height should be positive integers')

    file_format_to_use = (output_file_format if 
        output_file_format is not None else
        get_input_filepath_format(input_filepath)
    )

    output_filepath = str(merge_path_and_filename(
        get_filepath_parents(input_filepath),
        f'{output_filename}.{file_format_to_use}'
    ))

    return [input_filepath, '-resize', f'{scale_width}x{scale_height}{operator}', output_filepath]

