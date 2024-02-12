"""Documenter module for codergpt."""

from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable

from codergpt.constants import DOCS_DIR


class CodeDocumenter:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeDocumenter class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def document(
        self,
        filename: Union[str, Path],
        outfile: Optional[str] = None,
    ):
        """
        Document the contents of the code file by invoking the runnable chain.

        :param code: The string containing the code to be documented.
        :param function: The name of the function to document. Default is None.
        :param classname: The name of the class to document
        """
        with open(filename, "r") as source_file:
            source_code = source_file.read()
        response = self.chain.invoke(
            {
                "input": f"Document the following code: \n\n```\n{source_code}\n```"
                "This should be in reStructuredText (RST, ReST, or reST)"
                " format that is Sphinx compatible. Return only the documentation content."
            }
        )

        # Extract the commented code from the response if necessary
        documentation = response.content
        if outfile:
            destination_path = outfile
        else:
            destination_path = DOCS_DIR / f"{filename.stem}.rst"
        # Write the documentation to the new file
        with open(destination_path, "w") as updated_file:
            updated_file.write(documentation)
