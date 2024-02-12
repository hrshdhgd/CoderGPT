The ExpressionEvaluator Class
=============================

The ExpressionEvaluator class is designed for evaluating code expressions and extracting the source code of specified functions or classes from a given source code input. It utilizes the Abstract Syntax Tree (AST) provided by Python's ``ast`` module to navigate and interpret the structure of the code.

.. code-block:: python

    from expression_evaluator import ExpressionEvaluator

Initialization
--------------

To initialize an instance of the ExpressionEvaluator class, the source code to be analyzed needs to be provided, along with optional parameters specifying the names of the function or class to extract.

.. code-block:: python

    evaluator = ExpressionEvaluator(source_code, function_name="my_function", class_name="MyClass")

Parameters:

- ``source_code``: The complete source code as a string.
- ``function_name``: Optional. The name of the function to find and extract from the source code.
- ``class_name``: Optional. The name of the class to find and extract from the source code.

Attributes
----------

- ``function_code``: After evaluation, this attribute contains the extracted source code of the specified function, if found.
- ``class_code``: After evaluation, this attribute contains the extracted source code of the specified class, if found.
- ``function_name``: The name of the function to search for in the source code.
- ``class_name``: The name of the class to search for in the source code.
- ``source_code``: The source code provided during initialization.

Methods
-------

visit_FunctionDef
^^^^^^^^^^^^^^^^^

This method is called when a function definition node is encountered in the AST. If the name of the function matches the target function name specified during initialization, the source segment of the function is extracted.

.. code-block:: python

    def visit_FunctionDef(self, node):
        ...

Parameters:

- ``node``: An instance of ``ast.FunctionDef`` representing a function definition node in the AST.

visit_ClassDef
^^^^^^^^^^^^^^

This method is called when a class definition node is encountered in the AST. If the name of the class matches the target class name specified during initialization, the source segment of the class is extracted.

.. code-block:: python

    def visit_ClassDef(self, node):
        ...

Parameters:

- ``node``: An instance of ``ast.ClassDef`` representing a class definition node in the AST.

Usage
-----

To utilize the ExpressionEvaluator class, an instance must be created with the source code and optionally the function or class name. After initialization, the Abstract Syntax Tree is traversed, and if the specified function or class is found, its source code is extracted and stored in the ``function_code`` or ``class_code`` attributes respectively.

Example:

.. code-block:: python

    source = '''
    def hello_world():
        print("Hello, world!")

    class Greeter:
        def greet(self):
            print("Hello, world!")
    '''

    evaluator = ExpressionEvaluator(source, function_name="hello_world")
    ast.parse(source)
    evaluator.visit(ast.parse(source))

    print(evaluator.function_code)
    # Output: def hello_world():\n    print("Hello, world!")

This class provides a straightforward way to extract specific portions of code from a larger source code base, leveraging the power of Python's AST for code analysis and manipulation.
