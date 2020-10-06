from typing import NamedTuple


class LoggingConfig(NamedTuple):
    """data class representing logging configuration

    Args:
        NamedTuple (NamedTuple): base class
    """

    log_level: int
    log_format: str
    log_output_filepath: str


LOGGING = LoggingConfig(
    log_level=20,
    log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    log_output_filepath="/tmp/image_convert_facade.log",
)
