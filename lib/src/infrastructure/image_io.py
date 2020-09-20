from typing import Optional
from imghdr import what as what_image_format_is_this
from pathlib import Path
from subprocess import (
    PIPE,
    run,
)


def merge_path_and_filename(path, filename):
    return Path(path).joinpath(filename)


def get_filepath_parents(filepath):
    return Path(filepath).parents[0]


def get_filetype(filepath: str) -> str:
    return Path(filepath).suffix


def get_file_path(filepath: str) -> str:
    return Path(filepath).parts


def get_image_file_format(filepath: str) -> str:
    return what_image_format_is_this(Path(filepath))


def does_file_exist(filepath: str) -> bool:
    return Path(filepath).exists()


def run_command(
    program: str,
    command: str,
    command_args: Optional[list] = [],
    **options: dict
    ) -> tuple:

    args = [program, command] + command_args

    completed_process = run(
        args=args,
        stdout=PIPE,
        stderr=PIPE,
        shell=False,
        check=False,
        universal_newlines=True,
        **options
    )

    command_successful = completed_process.returncode == 0

    return (
        command_successful,
        completed_process.stdout if command_successful else completed_process.stderr
    )
