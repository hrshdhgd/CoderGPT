.. _codergpt:

CoderGPT
========

What is it?
-----------

CoderGPT is a command line interface for generating/modifying code. It allows developers to 
enhance code by commenting, optimizing, documenting and adding tests to their projects using 
the power of LLM and GPT. This project is powered by `langchain <https://github.com/langchain-ai/langchain>`_.

Model Providers Implemented
---------------------------

The following model providers have been implemented in CoderGPT:

.. list-table::
   :widths: 75 25
   :header-rows: 1

   * - Provider
     - Status
   * - OpenAI (``gpt-3.5-turbo``, ``gpt-4``, ``gpt-4-turbo-preview`` (default))
     - ✓
   * - Google (``gemini-pro``)
     - ✓
   * - Anthropic (``Claude``)
     - Coming soon!


.. note::
   **NOTE**
   Before you begin using CoderGPT, you must set the ``OPENAI_API_KEY`` and ``GOOGLE_API_KEY`` environment variables on your machine. These keys are necessary for authentication with the respective APIs and are crucial for the operation of the language models.

.. code-block:: sh

   export OPENAI_API_KEY='your-api-key-here'
   export GOOGLE_API_KEY='your-api-key-here'

Replace ``your-api-key-here`` with your actual OpenAI and Google API keys. This step is crucial for the proper functioning of CoderGPT as it relies on OpenAI and Google APIs for generating and modifying code.

Installation
------------

To use the CoderGPT CLI, clone the repository and install the required dependencies.

.. code-block:: shell

    pip install codergpt

The most recent code and data can be installed directly from GitHub with:

.. code-block:: shell

    pip install git+https://github.com/hrshdhgd/CoderGPT.git

To install in development mode (using `poetry`), use the following:

.. code-block:: shell

    $ git clone git+https://github.com/hrshdhgd/CoderGPT.git
    $ cd CoderGPT
    $ poetry install

Command Line Interface (CLI)
----------------------------

Run the CLI using the following syntax:

.. code-block:: shell

    codergpt [OPTIONS] COMMAND [ARGS]...

Options
~~~~~~~

- ``-v, --verbose INTEGER``: Set verbosity level (0, 1, or 2).
- ``-q, --quiet``: Enable quiet mode.
- ``--version``: Display version information.
- ``--model [gpt-3.5-turbo | gpt-4 | gpt-4-turbo (default) | gemini-pro]``: Set the model provider to use.

Commands
~~~~~~~~

.. _inspect-command:
1. **inspect**: Inspect a package and display a file-language map.

   .. code-block:: shell

       codergpt --model <model-name> inspect <path>

   **Example**

   .. code-block:: shell

       $ codergpt --model gpt-4 inspect src/codergpt/
       Inspecting the code.
       File                                        Language
       ------------------------------------------  ----------
       src/codergpt/constants.py                   Python
       src/codergpt/__init__.py                    Python
       src/codergpt/cli.py                         Python
       ...

.. _explain-command:
2. **explain**: Explain a specific function or class within a package.

   .. code-block:: shell

       codergpt explain <path> [--function <function_name>] [--classname <class_name>]

   **Example**

   .. code-block:: shell

       $ codergpt explain src/codergpt/explainer/explainer.py --function explain
       Explanation for the code:
       This code defines a method called `explain` that takes in three parameters...

.. _comment-command:
3. **comment**: Add comments to the code in a package. The user has the choice to overwrite the file or create a new one.

   .. code-block:: shell

       codergpt comment <path> [--overwrite/--no-overwrite]

   **Example**

   - Let's consider a python file `greetings.py`:

     .. code-block:: python

         def greet(name):
             return f"Hello, {name}!"

         if __name__ == "__main__":
             user_name = "Alice"
             print(greet(user_name))

   .. code-block:: shell

       $ codergpt comment greetings.py --overwrite

   results in ....

   .. code-block:: python

       def greet(name):
           """
           Generates a greeting message for the given name.
           ...
           """

.. _optimize-command:
4. **optimize**: Optimizes and adds comments to the code in a package. The user has the choice to overwrite the file or create a new one.

   .. code-block:: shell

       codergpt optimize <path> [--overwrite/--no-overwrite]

   **Example**

   - Let's consider a python file `example.py`:

     .. code-block:: python

        # example.py

        def calculate_sum(numbers):
            result = 0
            for number in numbers:
                result += number
            return result

        class MathOperations:
            def multiply(self, a, b):
                answer = 0
                for i in range(b):
                    answer += a
                return answer

   .. code-block:: shell

       $ codergpt optimize example.py --overwrite

   results in ....

   .. code-block:: python

        # example.py

        """
        Optimized and Documented Code.
        """

        from typing import List


        def calculate_sum(numbers: List[int]) -> int:
            """
            Calculates the sum of a list of numbers.

            Parameters:
            numbers (List[int]): A list of integers.

            Returns:
            int: The sum of the numbers.

            """
            result = sum(numbers)
            return result


        class MathOperations:
            def multiply(self, a: int, b: int) -> int:
                """
                Multiplies two numbers.

                Parameters:
                a (int): The first number.
                b (int): The second number.

                Returns:
                int: The result of multiplying a and b.

                """
                answer = a * b
                return answer


        """
        Optimization:

        1. In the 'calculate_sum' function, we can use the built-in 'sum' function to calculate the sum of the numbers in the list. This is more efficient than manually iterating over the list and adding each number to the result.
        2. In the 'multiply' method of the 'MathOperations' class, we can directly multiply the two numbers using the '*' operator. This eliminates the need for a loop and improves performance.
        By using these optimizations, we improve the efficiency and readability of the code.
        """

.. _write-tests-command:
5. **write-tests**: Generates test cases for specified functions and/or classes within a Python code file.

   .. code-block:: shell

       codergpt write-tests <filename> [--function <function_name>] [--class <classname>] [--outfile <output_filename>]

   **Example**

   - Let's consider a Python file `example.py`:

     .. code-block:: python

        # example.py

        def add(a, b):
            return a + b

        class Calculator:
            def subtract(self, a, b):
                return a - b

   .. code-block:: shell

       $ codergpt write-tests example.py --function add --class Calculator

   results in the creation of test files that contain test cases for both the `add` function and the `Calculator` class. The content of the generated test files might look like this:

   .. code-block:: python

        import unittest
        from example import add, Calculator

        class TestAddFunction(unittest.TestCase):

            def test_addition(self):
                self.assertEqual(add(3, 4), 7)

        class TestCalculator(unittest.TestCase):

            def setUp(self):
                self.calc = Calculator()

            def test_subtract(self):
                self.assertEqual(self.calc.subtract(10, 5), 5)

   In this example, executing the command generates unit tests for the `add` function and the `Calculator` class defined in `example.py`. The tests verify whether the `add` function correctly computes the sum of two numbers and if the `Calculator`'s `subtract` method accurately performs subtraction.

.. _document-command:

6. **document**: Generates documentation for the specified code file by invoking a runnable chain that processes and explains the code.

.. code-block:: shell

   codergpt document <path> [--outfile <output_filename>]

**Example**

Consider a Python file named ``example.py``:

.. code-block:: python

   # example.py

   def add(a, b):
       """Add two numbers and return the result."""
       return a + b

   class Calculator:
       """A simple calculator class."""

       def subtract(self, a, b):
           """Subtract b from a and return the result."""
           return a - b

To generate documentation for ``example.py``, execute the following command:

.. code-block:: shell

   $ codergpt document example.py

This command will produce documentation files that include explanations for all functions and classes within the ``example.py`` file. By default, the output file will be named after the input file with an ``.rst`` extension and saved in the directory specified by ``DOCS_DIR``. If an ``<outfile>`` is provided, the documentation will be written to that file instead.

The content of the generated documentation files will vary based on the implementation of the ``CodeDocumenter.document`` method but would typically resemble the following structured documentation:

.. code-block:: rst

   add Function
   ------------

   .. autofunction:: example.add

   Calculator Class
   ----------------

   .. autoclass:: example.Calculator
      :members:

In this case, running the command produces ReStructuredText (RST) formatted documentation for the entire ``example.py`` file. The documentation includes detailed descriptions of the `add` function and the `Calculator` class, as well as any public methods of the class.

Development
-----------

The CLI is built using Python and the `click` library. Below is an example of how to define a new command:

.. code-block:: python

    import click
    from codergpt import CoderGPT

    coder = CoderGPT()

    @click.command()
    @click.argument('path', type=click.Path(exists=True))
    def new_command(path):
        # Command logic here
        pass
