"""Test writing module."""

import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable

from codergpt.constants import TEST_DIR


class CodeTester:
    """Code tester class writes testing code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeTester class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def write_tests(
        self,
        filename: Union[str, Path],
        function: Optional[str] = None,
        classname: Optional[str] = None,
        outfile: Optional[str] = None,
    ):
        """
        Write tests for the code by invoking the runnable chain.

        :param path: The path to the code file to be explained.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        with open(filename, "r") as source_file:
            source_code = source_file.read()
        if function or classname:
            if function:
                response = self.chain.invoke(
                    {
                        "input": f"Write tests for the function '{function}' in \n\n```\n{source_code}\n```"
                        "Return just the code block. Also explain the tests in a systematic way as a comment."
                    }
                )
            if classname:
                response = self.chain.invoke(
                    {
                        "input": f"Write tests for the class '{classname}' in \n\n```\n{source_code}\n```"
                        "Also explain the tests in a systematic way."
                    }
                )
        else:
            # Write tests for full code
            response = self.chain.invoke(
                {
                    "input": f"Write tests for the following code: \n\n```\n{source_code}\n```"
                    "Also explain the tests in a systematic way."
                }
            )
        test_code = response.content
        base_filename = os.path.basename(filename)
        if outfile:
            new_filepath = outfile
        else:
            new_filepath = f"{TEST_DIR}/test_{base_filename}"
        # Write the test to the new file
        with open(new_filepath, "w") as updated_file:
            updated_file.write(test_code)
