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

       """
       Optimized and Documented Code:
       ...
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
