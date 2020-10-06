from abc import (
    ABC,
    abstractmethod,
)
from imghdr import what as what_image_format_is_this
from pathlib import Path


class FileIO(ABC):
    """abstract/interface class concering file system interactions

    Args:
        ABC (ABC): abstract base class
    """

    def __init__(self):
        """class constructor"""
        pass

    @abstractmethod
    def does_filepath_exist(self, filepath: str) -> bool:
        """check whether a file, located at `filepath`, exists

        Args:
            filepath (str): the path to a file

        Raises:
            NotImplementedError: if this method has not been implemented

        Returns:
            bool: True if the file located at filepath exists
        """
        raise NotImplementedError


class RealFileIO(FileIO):
    def __init__(self):
        super().__init__()

    def does_filepath_exist(self, filepath: str) -> bool:
        return filepath and Path(filepath).exists()


class FakeFileIO(RealFileIO):
    def __init__(self, filepaths: list = []):
        super().__init__()
        self._filepaths = filepaths

    def does_filepath_exist(self, filepath: str) -> bool:
        return filepath and filepath in self._filepaths


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
        raise Exception(f"{filepath} is not an image")

    input_filepath_filetype = get_filetype(filepath)

    if input_filepath_format == "jpeg" and input_filepath_filetype == "jpg":
        input_filepath_format = input_filepath_filetype

    return input_filepath_format


def get_output_image_file_format_to_use(
    input_filepath: str, output_file_format: str
) -> str:
    return (
        output_file_format
        if output_file_format is not None
        else get_input_image_filepath_format(input_filepath)
    )


def get_output_image_filepath(
    input_filepath: str, output_filename: str, output_file_format=None
) -> str:
    file_format_to_use = get_output_image_file_format_to_use(
        input_filepath, output_file_format
    )
    return str(
        merge_path_and_filename(
            get_filepath_parents(input_filepath),
            f"{output_filename}.{file_format_to_use}",
        )
    )
