"""Command line interface for CoderGPT."""

import logging
from pathlib import Path
from typing import TextIO, Union

import click

from codergpt import __version__
from codergpt.main import CoderGPT

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.version_option(__version__)
def main(verbose: int, quiet: bool):
    """
    CLI for CoderGPT.

    :param verbose: Verbosity while running.
    :param quiet: Boolean to be quiet or verbose.
    """
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)


@main.command()
@click.argument("path", type=click.Path(exists=True))
def inspect(path: Union[str, Path, TextIO]):
    """Inspect package to show file-language-map."""
    coder = CoderGPT()
    coder.inspect_package(path=path)


if __name__ == "__main__":
    main()
