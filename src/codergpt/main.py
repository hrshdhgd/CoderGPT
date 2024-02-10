"""Main python file."""

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
from codergpt.optimizer.optimizer import CodeOptimizer


class CoderGPT:
    """CoderGPT class."""

    def __init__(self):
        """Initialize the CoderGPT class."""
        self.llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", "You are world class software developer."), ("user", "{input}")]
        )
        self.chain = self.prompt | self.llm

    def inspect_package(self, path: Union[str, Path]):
        """
        Inspecting the code and displaying a mapping of files to their languages in a table.

        :param path: The path to the package or directory.
        """
        print("Inspecting the code.")

        with open(EXTENSION_MAP_FILE, "r") as file:
            extension_to_language = yaml.safe_load(file)

        path = Path(path)

        file_language_list = []
        file_language_dict = {}

        if path.is_dir():
            for file in path.rglob("*.*"):
                language = extension_to_language["language-map"].get(file.suffix)
                if language is not None:
                    file_language_list.append((str(file), language))
                    file_language_dict[str(file)] = language

        elif path.is_file():
            language = extension_to_language["language-map"].get(path.suffix)
            if language is not None:
                file_language_list.append((str(path), language))
                file_language_dict[str(path)] = language

        else:
            print(f"The path {path} is neither a file nor a directory.")
            return {}

        print(tabulate(file_language_list, headers=INSPECTION_HEADERS))
        return file_language_dict

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

        language_map = self.inspect_package(filename)
        language = language_map.get(str(filename))
        search_term = function_name if function_name else class_name
        if search_term:
            response = self.chain.invoke(
                {
                    "input": f"Identify the structure of this {language} code \n{source_code}\n"
                    f" and give me only the code (no explanation) that corresponds"
                    f" to the {search_term} function or class."
                }
            )
            code = response.content
        else:
            code = source_code

        return (code, language)

    def explainer(self, path: Union[str, Path], function: str = None, classname=None):
        """
        Explains contents of the code file.

        :param path: The path to the code file.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        code_explainer = CodeExplainer(self.chain)
        code, language = self.get_code(filename=path, function_name=function, class_name=classname)
        code_explainer.explain(code, language)

    def commenter(self, path: Union[str, Path], overwrite: bool = False):
        """
        Add comments to the code file.

        :param path: The path to the code file.
        :param overwrite: Whether to overwrite the existing comments. Default is False.
        """
        code_commenter = CodeCommenter(self.chain)
        code, language = self.get_code(filename=path)
        code_commenter.comment(code=code, filename=path, overwrite=overwrite, language=language)

    def optimizer(self, path: Union[str, Path], function: str = None, classname=None, overwrite: bool = False):
        """
        Optimize the code file.

        :param path: The path to the code file.
        """
        code_optimizer = CodeOptimizer(self.chain)
        # code, language = self.get_code(filename=path, function_name=function, class_name=classname)
        code_optimizer.optimize(filename=path, function=function, classname=classname, overwrite=overwrite)

    def tester(self, path: Union[str, Path]):
        """
        Test the code file.

        :param path: The path to the code file.
        """
        pass


if __name__ == "__main__":
    coder = CoderGPT()
    coder.inspect_package("src")
