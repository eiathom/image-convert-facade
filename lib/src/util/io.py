import json
from typing import Any

from lib.src.util.file import does_filepath_exist


def load_json_data_from_file(json_filepath: str) -> Any:
    if does_filepath_exist(json_filepath):
        data = {}
        with open(json_filepath) as json_file:
            data = json.load(json_file)
        return data
    raise FileNotFoundError('file does not exist', json_filepath)

