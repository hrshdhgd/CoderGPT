"""Main python file."""

import ast
import os
from pathlib import Path
from typing import Optional, Union

import yaml
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from tabulate import tabulate

from codergpt.commenter.commenter import CodeCommenter
from codergpt.constants import EXTENSION_MAP_FILE, INSPECTION_HEADERS
from codergpt.explainer.explainer import CodeExplainer
from codergpt.utils.expression_evaluator import ExpressionEvaluator


class CoderGPT:
    """CoderGPT class."""

    def __init__(self):
        """Initialize the CoderGPT class."""
        # Initialize the ChatOpenAI object with an API key from the environment variables.
        self.llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
        # Create a prompt template with predefined messages to set the context for the AI.
        # Here, we tell the AI that it is a "world class software developer".
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", "You are world class software developer."), ("user", "{input}")]
        )
        # Combine the prompt template with the ChatOpenAI object to create a chain.
        # This chain will be used to send the input to the AI in the correct context.
        self.chain = self.prompt | self.llm

    def inspect_package(self, path: Union[str, Path]):
        """Inspecting the code and displaying a mapping of files to their languages in a table."""
        print("Inspecting the code.")

        with open(EXTENSION_MAP_FILE, "r") as file:
            extension_to_language = yaml.safe_load(file)

        # Convert path to Path object if it's a string
        path = Path(path)

        # Initialize an empty list to store the results
        file_language_list = []

        # Check if the path is a directory or a file
        if path.is_dir():
            # Iterate over all files in the directory and subdirectories
            for file in path.rglob("*.*"):
                language = extension_to_language["language-map"].get(file.suffix)
                if language is not None:
                    file_language_list.append((str(file), language))

        elif path.is_file():
            # Get the language for the single file
            language = extension_to_language["language-map"].get(path.suffix)
            if language is not None:
                file_language_list.append((str(path), language))

        else:
            print(f"The path {path} is neither a file nor a directory.")
            return

        # Display the results as a table
        print(tabulate(file_language_list, headers=INSPECTION_HEADERS))

    def get_code(
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
        else:
            return source_code

    def explainer(self, path: Union[str, Path], function: str = None, classname=None):
        """Explains contents of the code file."""
        # Ensure path is a string or Path object for consistency
        code_explainer = CodeExplainer(self.chain)
        code = self.get_code(filename=path, function_name=function, class_name=classname)
        code_explainer.explain(code)

    def commenter(self, path: Union[str, Path], overwrite: bool = False):
        """Explains contents of the code file."""
        # Ensure path is a string or Path object for consistency
        code_commenter = CodeCommenter(self.chain)
        code = self.get_code(filename=path)
        code_commenter.comment(code=code, filename=path, overwrite=overwrite)


if __name__ == "__main__":
    coder = CoderGPT()
    coder.inspect_package("src")
