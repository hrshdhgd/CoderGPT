"""
The ExpressionEvaluator Class.

Used for evaluating the code expression and extracting the source code of the specified function or class.
"""

import ast


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
