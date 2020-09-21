from imghdr import what as what_image_format_is_this
from pathlib import Path


def does_filepath_exist(filepath: str) -> bool:
    return filepath and Path(filepath).exists()


def merge_path_and_filename(path: str, filename: str) -> Path:
    return Path(path).joinpath(filename)


def get_filepath_parents(filepath: str) -> Path:
    return Path(filepath).parents[0]


def get_filetype(filepath: str) -> str:
    return Path(filepath).suffix


def get_image_file_format(filepath: str) -> str:
    return what_image_format_is_this(Path(filepath))


def get_input_image_filepath_format(filepath: str) -> str:

    input_filepath_format = get_image_file_format(filepath)

    if not input_filepath_format:
        raise Exception(f'{filepath} is not an image')

    input_filepath_filetype = get_filetype(filepath)

    if input_filepath_format == 'jpeg' and input_filepath_filetype == 'jpg':
        input_filepath_format = input_filepath_filetype

    return input_filepath_format


def get_output_image_file_format_to_use(input_filepath: str, output_file_format: str) -> str:
    return (output_file_format if 
        output_file_format is not None else
        get_input_image_filepath_format(input_filepath)
    )


def get_output_image_filepath(input_filepath: str, output_filename: str, output_file_format = None) -> str:
    file_format_to_use = get_output_image_file_format_to_use(input_filepath, output_file_format)
    return str(merge_path_and_filename(
        get_filepath_parents(input_filepath),
        f'{output_filename}.{file_format_to_use}'
    ))

