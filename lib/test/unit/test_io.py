from lib.src.util.io import FakeIO


def test_fakeio_overrides_realio_load():
    filepath = "/path/to/file.txt"
    filepaths = [filepath]
    filepath_data_mapper = {
        filepath: {
            "data": [
                {
                    "input_filepath": "images/image.png",
                    "scale": 25,
                    "output_filename": "scaled_image_25",
                },
                {
                    "input_filepath": "images/image.png",
                    "scale": 200,
                    "output_filename": "scaled_image_200",
                },
            ]
        }
    }
    io = FakeIO(filepaths=filepaths, filepath_data_mapper=filepath_data_mapper)
    assert io.load_json_data_from_file(filepath) == filepath_data_mapper.get(filepath)
