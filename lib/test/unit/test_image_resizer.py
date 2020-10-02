from lib.src.domain.image_resizer import (
    MagickProgram,
    ConvertCommand,
    ResizeOption,
)


def test_build_magick_program():
    resize = ResizeOption(200, 200)
    command = ConvertCommand("images/image.png", "scaled_image", options=[resize])
    magick = MagickProgram(command=command)

    assert magick.get_program_name() == "magick"
    assert magick.get_command() == command
    assert magick.get_command().get_command_name() == "convert"
    options = magick.get_command().get_options()
    assert len(options) == 1
    option = options[0]
    assert option == resize
    assert option.get_option_name() == "resize"
