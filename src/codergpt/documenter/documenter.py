"""Documenter module for codergpt."""

from typing import Any, Dict, Optional

from langchain_core.runnables.base import RunnableSerializable

from codergpt.constants import DOCS_DIR, TEMPLATES


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
        filename: str,
        code: str,
        language: Optional[str] = None,
        outfile: Optional[str] = None,
    ):
        """
        Document the contents of the code file by invoking the runnable chain.

        :param filename: filename of the code file.
        :param code: The string containing the code to be documented.
        :param language: Coding language of the file, defaults to None
        :param outfile: Destination filepath, defaults to None
        """
        document_template = None
        if language and language in TEMPLATES.keys():
            # Check if "document" key exists in the language template
            if "document" in TEMPLATES[language]:
                # Get the path to the document template
                document_template_path = TEMPLATES[language]["document"]
                with open(document_template_path, "r") as document_template_file:
                    document_template = document_template_file.read()
        if document_template:
            invoke_params = {
                "input": f"Document the {language} code with the following: \n{code}\n"
                f"Use template {document_template} as a style reference."
                "Everything in the template are placeholders. Return only the relevant documentation content."
            }
        else:
            invoke_params = {
                "input": f"Document the {language} code with the following: \n{code}\n"
                "Return only the documentation content."
            }
        response = self.chain.invoke(invoke_params)

        # Extract the commented code from the response if necessary
        documentation = response.content
        if outfile:
            destination_path = outfile
        else:
            destination_path = DOCS_DIR / f"{filename}.rst"
        # Write the documentation to the new file
        with open(destination_path, "w") as updated_file:
            updated_file.write(documentation)
