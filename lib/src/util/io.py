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


class IO(ABC):
    """using this class as an interface and abstraction for IO opertions"""

    def __init__(self):
        pass

    @abstractmethod
    def get_file_io(self) -> FileIO:
        """an IO abstraction requires a way in which to interact with files"""
        raise NotImplementedError

    @abstractmethod
    def load_data(self, data_location: str) -> dict:
        """load data to dict from `data_location`"""
        raise NotImplementedError

    def load_json_data_from_file(self, filepath: str) -> dict:
        if self.get_file_io().does_filepath_exist(filepath):
            return self.load_data(filepath)
        raise FileNotFoundError("file does not exist", filepath)


class RealIO(IO):
    def __init__(self):
        super().__init__()
        self._fileio = RealFileIO()

    def get_file_io(self) -> FileIO:
        return self._fileio

    def load_data(self, data_location: str) -> dict:
        data = {}
        with open(data_location) as json_file:
            data = json.load(json_file)
        return data


class FakeIO(RealIO):
    def __init__(self, filepaths: list = [], filepath_data_mapper: dict = {}):
        """`filepath_data_mapper`: mapping a filepath to a data dict"""
        super().__init__()
        self._filepath_data_mapper = filepath_data_mapper
        self._filepaths = filepaths

    def get_file_io(self) -> FileIO:
        return FakeFileIO(filepaths=self._filepaths)

    def load_data(self, data_location: str) -> dict:
        return self._filepath_data_mapper.get(data_location, {})
