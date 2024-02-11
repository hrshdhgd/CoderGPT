.. _codergpt:

CoderGPT
========

What is it?
-----------

CoderGPT is a command line interface for generating/modifying code. It allows developers to 
enhance code by commenting, optimizing, documenting and adding tests to their projects using 
the power of LLM and GPT. This project is powered by `langchain <https://github.com/langchain-ai/langchain>`_.

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

    code [OPTIONS] COMMAND [ARGS]...

Options
~~~~~~~

- ``-v, --verbose INTEGER``: Set verbosity level (0, 1, or 2).
- ``-q, --quiet``: Enable quiet mode.
- ``--version``: Display version information.

Commands
~~~~~~~~

1. **inspect**: Inspect a package and display a file-language map.

   .. code-block:: shell

       code inspect <path>

   **Example**

   .. code-block:: shell

       $ code inspect src/codergpt/
       Inspecting the code.
       File                                        Language
       ------------------------------------------  ----------
       src/codergpt/constants.py                   Python
       src/codergpt/__init__.py                    Python
       src/codergpt/cli.py                         Python
       ...

2. **explain**: Explain a specific function or class within a package.

   .. code-block:: shell

       code explain <path> [--function <function_name>] [--classname <class_name>]

   **Example**

   .. code-block:: shell

       $ code explain src/codergpt/explainer/explainer.py --function explain
       Explanation for the code:
       This code defines a method called `explain` that takes in three parameters...

3. **comment**: Add comments to the code in a package. The user has the choice to overwrite the file or create a new one.

   .. code-block:: shell

       code comment <path> [--overwrite/--no-overwrite]

   **Example**

   - Let's consider a python file `greetings.py`:

     .. code-block:: python

         def greet(name):
             return f"Hello, {name}!"

         if __name__ == "__main__":
             user_name = "Alice"
             print(greet(user_name))

   .. code-block:: shell

       $ code comment greetings.py --overwrite

   results in ....

   .. code-block:: python

       def greet(name):
           """
           Generates a greeting message for the given name.
           ...
           """

4. **optimize**: Optimizes and adds comments to the code in a package. The user has the choice to overwrite the file or create a new one.

   .. code-block:: shell

       code optimize <path> [--overwrite/--no-overwrite]

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

       $ code optimize example.py --overwrite

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
