"""Explainer Module."""

import ast
from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable

from codergpt.utils.expression_evaluator import ExpressionEvaluator


class CodeExplainer:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeExplainer class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def get_function_code(
        self, filename: str, function_name: Optional[str] = None, class_name: Optional[str] = None
    ) -> Optional[str]:
        """
        Extract and return the source code of the specified function or class from a file.

        :param filename: The path to the file containing the code.
        :param function_name: The name of the function to extract code for. Default is None.
        :param class_name: The name of the class to extract code for. Default is None.
        :return: The extracted source code of the specified function or class, if found.
        """
        with open(filename, "r") as source_file:
            source_code = source_file.read()

        # Parse the source code into an AST
        parsed_code = ast.parse(source_code)

        # Create a visitor instance and walk through the AST
        visitor = ExpressionEvaluator(source_code=source_code, function_name=function_name, class_name=class_name)
        visitor.visit(parsed_code)
        if function_name:
            return visitor.function_code
        elif class_name:
            return visitor.class_code

    def explain(self, path: Union[str, Path], function: Optional[str] = None, classname: Optional[str] = None):
        """
        Explain the contents of the code file by invoking the runnable chain.

        :param path: The path to the code file to be explained.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        if function:
            code = self.get_function_code(filename=path, function_name=function)
            response = self.chain.invoke({"input": f"Explain the following code: \n\n```\n{code}\n```"})

            # Pretty print the response
            print(f"Explanation for '{function}':\n{response.content}")
        elif classname:
            code = self.get_function_code(filename=path, class_name=classname)
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
