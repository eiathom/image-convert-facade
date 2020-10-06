from abc import (
    ABC,
    abstractmethod,
)
import json
from typing import Any

from lib.src.util.file import (
    FakeFileIO,
    FileIO,
    RealFileIO,
)


class OpenReadData:
    """`open` wrapper ContextManager"""

    def __init__(self, filename: str, data: dict = None):
        self.filename = filename
        self.is_dict = data is not None
        self.filelike_obj = data if self.is_dict else open(file=self.filename)

    def __enter__(self):
        return (
            self.filelike_obj.get(self.filename) if self.is_dict else self.filelike_obj
        )

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        if not self.is_dict:
            self.filelike_obj.close()


class IO(ABC):
    """using this class as an interface/abstraction for IO opertions

    Args:
        ABC (ABC): abstract base class
    """

    def __init__(self, fileio: FileIO):
        """class constructor

        Args:
            fileio (FileIO): a file system class object
        """
        self._fileio = fileio

    def get_file_io(self) -> FileIO:
        return self._fileio

    @abstractmethod
    def load_data(self, data_location: str) -> dict:
        """load data from `data_location` into a native `dict` object

        Args:
            data_location (str): the location of the data

        Raises:
            NotImplementedError: if this method is not implemented

        Returns:
            dict: data located parsed to a native dict object
        """
        raise NotImplementedError

    def load_json_data_from_file(self, filepath: str) -> dict:
        if self.get_file_io().does_filepath_exist(filepath):
            return self.load_data(filepath)
        raise FileNotFoundError("file does not exist", filepath)


class RealIO(IO):
    def __init__(self, fileio: FileIO = RealFileIO()):
        super().__init__(fileio=fileio)

    def load_data(self, data_location: str) -> dict:
        data = {}
        with open(data_location) as json_file:
            data = json.load(json_file)
        return data


class FakeIO(RealIO):
    """for testing purposes, we pass a test FileIO object to the IO
    implementation
    """

    def __init__(self, filepaths: list = [], filepath_data_mapper: dict = {}):
        """`filepaths`: a list of file locations for the FileIO to use

        `filepath_data_mapper`: mapping a filepath to a data dict
        """
        super().__init__(fileio=FakeFileIO(filepaths=filepaths))
        self._filepath_data_mapper = filepath_data_mapper
        self._filepaths = filepaths

    def load_data(self, data_location: str) -> dict:
        return self._filepath_data_mapper.get(data_location, {})
