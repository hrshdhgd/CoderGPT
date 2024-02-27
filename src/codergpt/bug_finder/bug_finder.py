"""Bug-finder class for the package."""

from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable

from codergpt.utils import extract_code_from_response


class BugFinder:
    """Bug-finder class for the package."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """Initialize the BugFinder class."""
        self.chain = chain

    def find_bugs(
        self, code: str, function: Optional[str] = None, classname: Optional[str] = None, language: Optional[str] = None
    ):
        """
        Find bugs in the given code.

        :param code: The code to find bugs in.
        :param function: The name of the function to find bugs in. Default is None.
        :param classname: The name of the class to find bugs in. Default is None.
        :param language: The language of the code. Default is None.
        """
        if function:
            response = self.chain.invoke(
                {
                    "input": f"Find and list all the bugs in the function {function}"
                    f" in the following {language} code: \n\n```\n{code}\n```"
                }
            )
            # Pretty print the response
            print(f"Bugs found in '{function}':\n{response.content}")
        elif classname:
            response = self.chain.invoke(
                {
                    "input": f"Find and list all the bugs in the class {classname}"
                    f" in the following {language} code: \n\n```\n{code}\n```"
                }
            )
            # Pretty print the response
            print(f"Bugs found in '{classname}':\n{response.content}")
        else:
            # Find bugs in full code
            response = self.chain.invoke(
                {"input": f"Find and list all the bugs in the following {language} code: \n\n```\n{code}\n```"}
            )
            # Pretty print the response
            print(f"Bugs found in the code:\n{response.content}")

    def fix_bugs(
        self,
        filename: Union[str, Path],
        code: str,
        function: Optional[str] = None,
        classname: Optional[str] = None,
        language: Optional[str] = None,
        outfile: Optional[str] = None,
    ) -> None:
        """
        Fix bugs in the given code.

        :param code: The code to fix bugs in.
        :param function: The name of the function to fix bugs in. Default is None.
        :param classname: The name of the class to fix bugs
        :param outfile:Path for output file with bug-fix code. Default is None.
        """
        if function:
            response = self.chain.invoke(
                {
                    "input": f"List all the bug fixes if any and rewrite the function {function}"
                    f" in the following {language} code: \n\n```\n{code}\n```"
                }
            )
            # Pretty print the response
            print(f"Fixed code for '{function}':\n{response.content}")
            return response.content
        elif classname:
            response = self.chain.invoke(
                {
                    "input": f"List all the bug fixes if any and rewrite the class {classname}"
                    f" in the following {language} code: \n\n```\n{code}\n```"
                }
            )
            # Pretty print the response
            print(f"Fixed code for '{classname}':\n{response.content}")
            return response.content
        else:
            # Fix bugs in full code
            response = self.chain.invoke(
                {
                    "input": f"List all the bug fixes if any and rewrite the following {language}"
                    f" code: \n\n```\n{code}\n```"
                }
            )
            return extract_code_from_response(language, response.content, filename, outfile)
