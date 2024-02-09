"""
Command line interface for CoderGPT.

Author: Harshad Hegde

This module provides a command line interface (CLI) for CoderGPT, a powerful code generation tool.

Usage:
    python codergpt_cli.py [OPTIONS] COMMAND [ARGS]...

Options:
    -v, --verbose INTEGER    Verbosity level (0, 1 or 2).
    -q, --quiet              Run in quiet mode.
    --version                Show the version and exit.

Commands:
    inspect     Inspect package to show file-language-map.
    explain     Inspect package to show file-language-map.
    comment     Inspect package to show file-language-map.

"""

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
overwrite_option = click.option(
    "--overwrite/--no-overwrite", is_flag=True, default=False, help="Overwrite the existing file."
)

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
    """
    Inspect package to show file-language-map.

    :param path: Path to the package.
    """
    coder.inspect_package(path=path)

@main.command()
@path_argument
@click.option("-f", "--function", help="Function name to explain.")
@click.option("-c", "--classname", help="Class name to explain.")
def explain(path: Union[str, Path], function: str, classname: str):
    """
    Inspect package to show file-language-map.

    :param path: Path to the package.
    :param function: Name of the function to explain.
    :param classname: Name of the class to explain.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.explainer(path=path, function=function, classname=classname)
    else:
        raise ValueError("The path provided is not a file.")

@main.command("comment")
@path_argument
@overwrite_option
def add_comments(path: Union[str, Path], overwrite: bool = False):
    """
    Inspect package to show file-language-map.

    :param path: Path to the package.
    :param overwrite: Flag to indicate whether to overwrite existing files.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.commenter(path=path, overwrite=overwrite)
    else:
        raise ValueError("The path provided is not a file.")

if __name__ == "__main__":
    main()
