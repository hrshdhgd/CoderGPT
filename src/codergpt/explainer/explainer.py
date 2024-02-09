"""Explainer Module."""

from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable


class CodeExplainer:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeExplainer class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def explain(self, path: Union[str, Path], function: Optional[str] = None, classname: Optional[str] = None):
        """
        Explain the contents of the code file by invoking the runnable chain.

        :param path: The path to the code file to be explained.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        if function:
            code = self.get_code(filename=path, function_name=function)
            response = self.chain.invoke({"input": f"Explain the following code: \n\n```\n{code}\n```"})

            # Pretty print the response
            print(f"Explanation for '{function}':\n{response.content}")
        elif classname:
            code = self.get_code(filename=path, class_name=classname)
            response = self.chain.invoke({"input": f"Explain the following code: \n\n```\n{code}\n```"})
            # Pretty print the response
            print(f"Explanation for '{classname}':\n{response.content}")
        else:
            # Explain full code
            with open(path, "r") as file:
                code = file.read()
            response = self.chain.invoke({"input": f"Explain the following code: \n\n```\n{code}\n```"})
            # Pretty print the response
            print(f"Explanation for the code:\n{response.content}")
