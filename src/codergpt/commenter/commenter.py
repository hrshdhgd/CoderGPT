"""Commenter Module."""

import os
from typing import Any, Dict, Optional

from langchain_core.runnables.base import RunnableSerializable

from codergpt.constants import TEMPLATES


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
        :param language: Coding language of the file, defaults to None
        """
        comment_template = None
        if language and language in TEMPLATES.keys():
            # Check if "comment" key exists in the language template
            if "comment" in TEMPLATES[language]:
                # Get the path to the comment template
                comment_template_path = TEMPLATES[language]["comment"]
                with open(comment_template_path, "r") as comment_template_file:
                    comment_template = comment_template_file.read()

        if comment_template:
            invoke_params = {
                "input": f"Rewrite and return this {language} code with\
                comments: \n{code}\n"
                f"Use template {comment_template} as a style reference to render the docstrings."
                "Everything in the template are placeholders."
                "Return just the code block since all this will be saved in a file."
            }
        else:
            invoke_params = {
                "input": f"Rewrite and return this {language} code with\
                    comments: \n{code}\n"
                "Return just the code block since all this will be a file."
            }

        response = self.chain.invoke(invoke_params)

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
