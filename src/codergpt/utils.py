"""Utility functions for the codergpt package."""

import os
import re
from pathlib import Path
from typing import Optional, Union

import yaml

from codergpt.constants import EXTENSION_MAP_FILE


def extract_code_from_response(
    language: str, response: str, filename: Union[str, Path], outfile: Optional[str] = None
) -> str:
    """
    Generate code files based on LLM responses.

    :param language: Code language.
    :param response: LLM response.
    :param filename: Source code file.
    :param outfile: Destination filepath, defaults to None
    """
    base, ext = os.path.splitext(filename)
    file_parent = Path(filename).parent

    if not language:
        get_language_from_extension(filename)

    code_pattern_block = rf"```{language.lower()}(.*?)(?<=\n)```"
    matches = re.findall(code_pattern_block, response, re.DOTALL)

    if matches:
        code_to_save = matches[0].strip()
        if not outfile:
            outfile = f"{file_parent/base}_updated{ext}"
        with open(outfile, "w") as file:
            file.write(code_to_save)
        print(f"Fixed code saved in file: {outfile}")

    print(response)
    return response


def get_language_from_extension(filename: Union[str, Path]) -> Optional[str]:
    """
    Get the language of a file from its extension.

    :param filename: The filename to get the language for.
    :return: The language of the file, if found.
    """
    with open(EXTENSION_MAP_FILE, "r") as file:
        extension_to_language = yaml.safe_load(file)
    language = extension_to_language["language-map"].get(Path(filename).suffix)
    return language
