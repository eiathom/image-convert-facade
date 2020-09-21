from lib.src.domain.image_resizer import (
    MagickProgram,
    ConvertCommand,
    ResizeOption,
)


def test_default_args():
    resize = ResizeOption(200, 200)
    command = ConvertCommand('images/image.png', 'scaled_image', options=[resize])
    magick = MagickProgram(command=command)

    assert magick.get_program_name() == 'magick'
