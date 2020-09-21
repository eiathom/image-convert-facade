from typing import Optional
from subprocess import (
    PIPE,
    run,
)

from lib.src.domain.image_resizer import Program


def run_command(program: Program, **options: Optional[dict]) -> tuple:

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

    return (
        command_successful,
        completed_process.stdout if command_successful else completed_process.stderr
    )
