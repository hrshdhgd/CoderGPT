```python
#!/usr/bin/env python3
"""
Module docstring for the example Python script.

This script provides an example of a Python module including various structures such as classes, functions,
decorators, and more, with appropriate docstrings and comments.
"""

# Import statements
import os
import sys

# Global variables
GLOBAL_CONSTANT = 42

def function_with_types_in_docstring(param1, param2):
    """
    Example of a function with types specified in the :param: format.

    :param param1: The first parameter.
    :type param1: int
    :param param2: The second parameter.
    :type param2: str
    :return: The return value. True for success, False otherwise.
    :rtype: bool
    """
    return True

def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """
    Example of a function with PEP 484 type annotations.

    :param param1: The first parameter.
    :param param2: The second parameter.
    :return: The return value. True for success, False otherwise.
    """
    return True

class ExampleClass:
    """
    This is an example class with a simple docstring.

    :ivar attr1: Description of `attr1`.
    :vartype attr1: str
    :ivar attr2: Description of `attr2`, defaults to 0.
    :vartype attr2: int, optional
    """

    def __init__(self, attr1: str, attr2: int = 0):
        """
        The constructor for ExampleClass.

        :param attr1: The first attribute.
        :type attr1: str
        :param attr2: The second attribute. Defaults to 0.
        :type attr2: int, optional
        """
        self.attr1 = attr1
        self.attr2 = attr2

    def example_method(self, param1):
        """
        An example method.

        :param param1: The first parameter of the method.
        :type param1: str
        :return: The return value. True for success, False otherwise.
        :rtype: bool
        """
        return True

    @staticmethod
    def static_example_method(param1):
        """
        An example of a static method.

        :param param1: The first parameter of the method.
        :type param1: str
        :return: The return value. True for success, False otherwise.
        :rtype: bool
        """
        return True

    @classmethod
    def class_example_method(cls, param1):
        """
        An example of a class method.

        :param param1: The first parameter of the method.
        :type param1: str
        :return: The return value. True for success, False otherwise.
        :rtype: bool
        """
        return True

    @property
    def example_property(self):
        """
        An example of a property.

        :return: The current value of `attr1`.
        :rtype: str
        """
        return self.attr1

    @example_property.setter
    def example_property(self, value):
        """
        The setter for `example_property`.

        :param value: The new value for `attr1`.
        :type value: str
        """
        self.attr1 = value

# Decorators
def decorator_function(original_function):
    """
    A simple decorator function that wraps the input function.

    :param original_function: The function to decorate.
    :type original_function: callable
    :return: The wrapped function.
    :rtype: callable
    """
    def wrapper_function(*args, **kwargs):
        # Do something before the original function is called.
        result = original_function(*args, **kwargs)
        # Do something after the original function is called.
        return result
    return wrapper_function

@decorator_function
def function_to_decorate():
    """
    Example function that will be decorated.
    """
    pass

# Conditional execution
if __name__ == "__main__":
    # Code to execute when the script is run directly
    example_instance = ExampleClass("Hello", 123)
    print(example_instance.example_method("World"))
```