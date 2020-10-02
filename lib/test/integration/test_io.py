from lib.src.util.io import RealIO


def test_reading_data_from_disk():
    actual_filepath = "data/images.json"
    expected_data = {
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
    io = RealIO()
    assert io.load_json_data_from_file(actual_filepath) == expected_data
