"""Optimizer Module."""

import os
from typing import Any, Dict, Optional

from langchain_core.runnables.base import RunnableSerializable


class CodeOptimizer:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeExplainer class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def optimize(
        self,
        filename: str,
        function: Optional[str] = None,
        classname: Optional[str] = None,
        overwrite: bool = False,
    ):
        """
        Optimize the the code by invoking the runnable chain.

        :param path: The path to the code file to be explained.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        with open(filename, "r") as source_file:
            source_code = source_file.read()
        if function:
            response = self.chain.invoke(
                {
                    "input": f"Optimize, comment and add sphinx docstrings"
                    f" to the function '{function}' in \n\n```\n{source_code}\n```"
                    "Also explain the optimization ina systematic way."
                }
            )
        elif classname:
            response = self.chain.invoke(
                {
                    "input": f"Optimize, comment and add sphinx docstrings"
                    f" to the class '{classname}' in \n\n```\n{source_code}\n```"
                    "Also explain the optimization ina systematic way."
                }
            )
        else:
            # Explain full code
            response = self.chain.invoke(
                {
                    "input": f"Optimize, comment and add sphinx style docstrings"
                    f" to the following code: \n\n```\n{source_code}\n```"
                    "Also explain the optimization ina systematic way."
                }
            )
        optimized_code = response.content
        new_filename = filename
        if not overwrite:
            # Create a new filename with the _updated suffix
            base, ext = os.path.splitext(filename)
            new_filename = f"{base}_updated{ext}"

        # Write the commented code to the new file
        with open(new_filename, "w") as updated_file:
            updated_file.write(optimized_code)
