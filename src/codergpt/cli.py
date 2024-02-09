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

path_argument = click.argument("path", type=click.Path(exists=True))

coder = CoderGPT()


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
@path_argument
def inspect(path: Union[str, Path, TextIO]):
    """Inspect package to show file-language-map."""
    coder.inspect_package(path=path)


@main.command()
@path_argument
@click.option("-f", "--function", help="Function name to explain.")
@click.option("-c", "--classname", help="Class name to explain.")
def explain(path: Union[str, Path], function: str, classname: str):
    """Inspect package to show file-language-map."""
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.explainer(path=path, function=function, classname=classname)
    else:
        raise ValueError("The path provided is not a file.")


if __name__ == "__main__":
    main()