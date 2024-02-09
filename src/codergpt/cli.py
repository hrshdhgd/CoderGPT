"""Command line interface for CoderGPT."""

import logging

import click

from codergpt import __version__
from codergpt.main import start

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
def run():
    """Run the CoderGPT's demo command."""
    start()


def explore():
    """Explore the code."""
    print("Exploring the code.")


if __name__ == "__main__":
    main()
