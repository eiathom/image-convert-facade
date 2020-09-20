from lib.src.domain.image_resizer import (
    do_convert_image,
    do_scale_image,
    get_command_args,
    OPERATORS,
    PERCENT_OPERATOR,
)


def test_do_convert_image():
    input_filepath = 'images/image.png'
    output_filename = 'converted_image'
    output_file_format='jpg'
    do_convert_image(
        input_filepath=input_filepath,
        output_filename=output_filename,
        output_file_format=output_file_format
    )


def test_do_scale_image():
    input_filepath = 'images/image.png'
    output_filename = 'scaled_image'
    scale = 0
    do_scale_image(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale=scale
    )


def test_get_command_args():
    input_filepath = 'images/image.png'
    scale = 0
    output_filename = 'scaled_image'
    expected_args = [
        input_filepath,
        '-resize',
        f'{scale}x{scale}%',
        f'images/{output_filename}.tiff'
    ]
    actual_args = get_command_args(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale_width=scale,
        scale_height=scale,
        operator=OPERATORS.get(PERCENT_OPERATOR),
        output_file_format='tiff'
    )
    assert actual_args == expected_args
