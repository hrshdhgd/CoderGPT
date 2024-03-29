"""
Command line interface for CoderGPT.

Author: Harshad Hegde

This module provides a command line interface (CLI) for CoderGPT, a powerful code generation tool.

Usage:
    codergpt [OPTIONS] COMMAND [ARGS]...

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
from codergpt.constants import ALL_MODELS
from codergpt.main import CoderGPT

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)

path_argument = click.argument("path", type=click.Path(exists=True))
model_option = click.option(
    "-m",
    "--model",
    type=click.Choice(ALL_MODELS),
    default="gpt-4",
    help="Model to use for code generation.",
)
prompt_option = click.option(
    "-p",
    "--prompt",
    type=Union[str, Path],
    help="Prompt to use for code generation.",
)
function_option = click.option("-f", "--function", help="Function name to explain or optimize.")
class_option = click.option("-c", "--classname", help="Class name to explain or optimize.")
overwrite_option = click.option(
    "--overwrite/--no-overwrite", is_flag=True, default=False, help="Overwrite the existing file."
)
output_option = click.option("-o", "--outfile", help="Output file to write to.")


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.version_option(__version__)
@model_option
def main(verbose: int, quiet: bool, model: str):
    """
    CLI for CoderGPT.

    :param verbose: Verbosity while running.
    :param quiet: Boolean to be quiet or verbose.
    """
    global coder
    coder = CoderGPT(model=model)
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
@function_option
@class_option
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


@main.command("optimize")
@path_argument
@function_option
@class_option
@overwrite_option
def optimize_code(path: Union[str, Path], function: str, classname: str, overwrite: bool = False):
    """
    Optimize the code file.

    :param path: The path to the code file.
    :param function: The name of the function to optimize. Default is None.
    :param classname: The name of the class to optimize. Default is None.
    :param overwrite: Whether to overwrite the existing file. Default is False.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.optimizer(path=path, function=function, classname=classname, overwrite=overwrite)
    else:
        raise ValueError("The path provided is not a file.")


@main.command("write-tests")
@path_argument
@function_option
@class_option
@output_option
def write_test_code(path: Union[str, Path], function: str, classname: str, outfile: Union[str, Path] = None):
    """
    Write tests for the code file.

    :param path: The path to the code file.
    :param function: The name of the function to test. Default is None.
    :param classname: The name of the class to test. Default is None.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.test_writer(path=path, function=function, classname=classname, outfile=outfile)
    else:
        raise ValueError("The path provided is not a file.")


@main.command("document")
@path_argument
@output_option
def write_documentation(path: Union[str, Path], outfile: Union[str, Path] = None):
    """
    Write documentation files for the code file.

    :param path: The path to the code file.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.documenter(path=path, outfile=outfile)
    else:
        raise ValueError("The path provided is not a file.")


@main.command("find-bugs")
@path_argument
@function_option
@class_option
def find_bugs_in_code(path: Union[str, Path], function: str, classname: str):
    """
    Write tests for the code file.

    :param path: The path to the code file.
    :param function: The name of the function to test. Default is None.
    :param classname: The name of the class to test. Default is None.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.bug_finder(path=path, function=function, classname=classname)
    else:
        raise ValueError("The path provided is not a file.")


@main.command("fix-bugs")
@path_argument
@function_option
@class_option
@output_option
def fix_bugs_in_code(path: Union[str, Path], function: str, classname: str, outfile: Union[str, Path] = None):
    """
    Write tests for the code file.

    :param path: The path to the code file.
    :param function: The name of the function to test. Default is None.
    :param classname: The name of the class to test. Default is None.
    """
    # Ensure path is a string or Path object for consistency
    if isinstance(path, str):
        path = Path(path)

    # Check if path is a file
    if path.is_file():
        coder.bug_fixer(path=path, function=function, classname=classname, outfile=outfile)
    else:
        raise ValueError("The path provided is not a file.")


if __name__ == "__main__":
    main()
