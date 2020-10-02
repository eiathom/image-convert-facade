from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Optional,
    List,
)


from lib.src.util.file import get_output_image_filepath


class Option(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_option_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_option_argument(self) -> list:
        raise NotImplementedError


Options = List[Option]  # type


class ResizeOption(Option):
    PERCENT_OPERATOR = "PERCENT"
    OPERATORS = {PERCENT_OPERATOR: "%"}

    def __init__(
        self,
        scale_width: int,
        scale_height: int,
        operator: Optional[str] = OPERATORS.get(PERCENT_OPERATOR),
    ):
        super().__init__()
        self.scale_width = scale_width
        self.scale_height = scale_height
        self.operator = operator
        self._option_name = "resize"

    def get_option_name(self) -> str:
        return self._option_name

    def get_scale_width(self) -> int:
        return self.scale_width

    def get_scale_height(self) -> int:
        return self.scale_height

    def get_operator(self) -> str:
        return self.operator

    def get_option_argument(self) -> list:
        return [
            f"-{self.get_option_name()}",
            f"{self.get_scale_width()}x{self.get_scale_height()}{self.get_operator()}",
        ]

    def __repr__(self):
        return f"ResizeOption(scale_width: {self.scale_width}, scale_height: {self.scale_height})"

    def __str__(self):
        return f"scale_width: {self.scale_width}, scale_height: {self.scale_height}"


class Command(ABC):
    def __init__(self, options: Optional[Options]):
        self.options = options if options else []

    def get_options(self) -> Options:
        return self.options

    def get_flattened_options(self):
        nested_options = [
            options.get_option_argument() for options in self.get_options()
        ]
        flattened_options = [option for options in nested_options for option in options]
        return flattened_options

    @abstractmethod
    def get_command_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_command_options(self) -> list:
        raise NotImplementedError


class ConvertCommand(Command):
    def __init__(
        self,
        input_filepath: str,
        output_filename: str,
        options: Optional[Options] = None,
        output_file_format: Optional[str] = None,
    ):
        super().__init__(options)
        self.input_filepath = input_filepath
        self.output_filename = output_filename
        self.output_file_format = output_file_format
        self._command_name = "convert"

    def get_command_name(self) -> str:
        return self._command_name

    def get_input_filepath(self) -> str:
        return self.input_filepath

    def get_output_filename(self) -> str:
        return self.output_filename

    def get_output_file_format(self):
        return self.output_file_format

    def get_output_filepath(self):
        return get_output_image_filepath(
            self.get_input_filepath(),
            self.get_output_filename(),
            self.get_output_file_format(),
        )

    def get_command_options(self) -> list:
        command_options = self.get_flattened_options()
        command_options.insert(0, self.get_command_name())
        command_options.insert(1, self.get_input_filepath())
        command_options.append(self.get_output_filepath())
        return command_options

    def __repr__(self):
        return f"ConvertCommand(input_filepath:{self.input_filepath}, output_filename:{self.output_filename})"

    def __str__(self):
        return f"input_filepath: {self.input_filepath}, output_filename: {self.output_filename}"


class Program(ABC):
    def __init__(self, command: Command):
        self.command = command

    def get_command(self) -> Command:
        return self.command

    def get_program_command(self) -> list:
        commands = self.get_command().get_command_options()
        commands.insert(0, self.get_program_name())
        return commands

    @abstractmethod
    def get_program_name(self) -> str:
        raise NotImplementedError


class MagickProgram(Program):
    def __init__(self, command: Command):
        super().__init__(command)
        self._program_name = "magick"

    def get_program_name(self) -> str:
        return self._program_name

    def __repr__(self):
        return f"MagickProgram(command: {self.command})"

    def __str__(self):
        return f"command: {self.command}"
