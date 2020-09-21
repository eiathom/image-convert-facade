from typing import Optional
from subprocess import (
    PIPE,
    run,
)

from lib.src.domain.image_resizer import Program
from lib.src.util.logger import get_logger


logger = get_logger(__name__)


def run_command(program: Program, **options: Optional[dict]) -> tuple:
    logger.info(f'running program: {program} with options: {options}')

    completed_process = run(
        args=program.get_program_command(),
        stdout=PIPE,
        stderr=PIPE,
        shell=False,
        check=False,
        universal_newlines=True,
        **options
    )

    command_successful = completed_process.returncode == 0
    logger.info(f'command success: {command_successful}')

    return (
        command_successful,
        completed_process.stdout if command_successful else completed_process.stderr
    )
