"""gpt-image-cli — OpenAI GPT Image 2 command-line interface."""

from __future__ import annotations

from typing import NoReturn

__all__ = ["main"]
__version__ = "0.3.0"


def main() -> int | NoReturn:
    """Lazily import the CLI entrypoint to avoid `python -m` double-import warnings."""
    from .cli import main as cli_main

    return cli_main()
