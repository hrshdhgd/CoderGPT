"""Explainer Module."""

import ast
from pathlib import Path
from typing import Any, Dict, Optional, Union

from langchain_core.runnables.base import RunnableSerializable


class ExpressionEvaluator(ast.NodeVisitor):
    """Evaluate the code expression and extract the source code of the specified function or class."""

    def __init__(self, source_code, function_name=None, class_name=None):
        """
        Initialize the ExpressionEvaluator class.

        :param function_name: The name of the function to find in the source code.
        :type function_name: str or None
        :param class_name: The name of the class to find in the source code.
        :type class_name: str or None
        """
        self.function_code = None
        self.class_code = None
        self.function_name = function_name
        self.class_name = class_name
        self.source_code = source_code

    def visit_FunctionDef(self, node):
        """
        Visit a FunctionDef (function definition) node in the AST.

        If the function name matches the target function name, it extracts the source segment.

        :param node: The node representing a function definition in the AST.
        :type node: ast.FunctionDef
        """
        if self.function_name == node.name:
            self.function_code = ast.get_source_segment(self.source_code, node)
        # Continue the traversal in case there are nested functions or classes
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """
        Visit a ClassDef (class definition) node in the AST.

        If the class name matches the target class name, it extracts the source segment.

        :param node: The node representing a class definition in the AST.
        :type node: ast.ClassDef
        """
        if self.class_name == node.name:
            self.class_code = ast.get_source_segment(self.source_code, node)
        # Continue the traversal in case there are nested functions or classes
        self.generic_visit(node)


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

        # # Ensure path is a string or Path object for consistency
        # if isinstance(path, str):
        #     path = Path(path)

        # with open(path, "r") as file:
        #     code = file.read()

        # # Guess the lexer based on the file name and content
        # lexer = guess_lexer_for_filename(path.name, code)

        # # Tokenize the code using the guessed lexer
        # tokens = list(pygments.lex(code, lexer))

        # all_functions = []
        # all_classes = []
        # # Process the tokens (for demonstration, just print them)
        # for token_type, token_value in tokens:
        #     if token_type in Token.Name.Function:
        #         print(f"{token_type}: {token_value}")
        #         all_functions.append(token_value)
        #     elif token_type in Token.Name.Class:
        #         all_classes.append(token_value)
        #     else:
        #         continue

        # elif token_type in Token.Comment:
        #     print(f"Comment: {token_value}")
        # Add more conditions as needed to handle different parts of the code
