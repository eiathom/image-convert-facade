from lib.src.domain.image_resizer import do_scale_image


def scale_images(data: dict) -> tuple:
    pass


def scale_image(
    input_filepath: str,
    output_filename: str,
    scale: int
    ) -> tuple:

    return do_scale_image(
        input_filepath=input_filepath,
        output_filename=output_filename,
        scale=scale
    )
