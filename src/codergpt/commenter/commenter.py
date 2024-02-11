"""Commenter Module."""

import os
from typing import Any, Dict, Optional

from langchain_core.runnables.base import RunnableSerializable


class CodeCommenter:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeExplainer class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def comment(self, code: str, filename: str, overwrite: bool = False, language: Optional[str] = None):
        """
        Comment the contents of the code string by invoking the runnable chain and write it to a new file.

        :param code: The string containing the code to be commented.
        :param filename: The original filename of the code file.
        :param overwrite: A boolean indicating whether to overwrite the original file. Default is False.
        """
        response = self.chain.invoke(
            {
                "input": f"Rewrite and return this {language} code with\
                comments and sphinx docstrings in :param: format: \n{code}\n"
            }
        )

        # Extract the commented code from the response if necessary
        commented_code = response.content

        new_filename = filename
        if not overwrite:
            # Create a new filename with the _updated suffix
            base, ext = os.path.splitext(filename)
            new_filename = f"{base}_updated{ext}"

        # Write the commented code to the new file
        with open(new_filename, "w") as updated_file:
            updated_file.write(commented_code)
