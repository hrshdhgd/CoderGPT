```
Command line interface for CoderGPT
====================================

This module provides a command line interface (CLI) for CoderGPT, a powerful code generation tool designed to assist in various coding tasks, including inspection, explanation, commenting, optimization, test writing, and documentation of code files.

.. moduleauthor:: Harshad Hegde

Usage
-----

To use this CLI, run the following command in your terminal:

.. code-block:: shell

    python codergpt_cli.py [OPTIONS] COMMAND [ARGS]...

Options
-------

-v, --verbose INTEGER
  Verbosity level, which can be set to 0, 1, or 2.

-q, --quiet
  Activate quiet mode, limiting output messages.

--version
  Display the current version of CoderGPT and exit.

Commands
--------

**inspect**
  Inspect a package to show a file-language map. Requires a path to the package as an argument.

**explain**
  Provide explanations for a specified function or class within a file. This command requires a path and can optionally include a function name and a class name.

**comment**
  Add comments to a code file. This command requires a path to the file and accepts an overwrite flag to indicate whether existing files should be overwritten.

**optimize**
  Optimize a code file by improving its performance or code quality. This command requires a path to the file and can optionally include a function name, a class name, and an overwrite flag.

**write-tests**
  Generate test cases for a specified function or class within a file. This command requires a path and can optionally include a function name and a class name.

**document**
  Write documentation files for a code file. This command requires a path to the file.

.. note:: All path arguments can be a string path, a :class:`pathlib.Path` object, or a file object.

Examples
--------

Inspect a package:

.. code-block:: shell

    python codergpt_cli.py inspect /path/to/package

Explain a function in a file:

.. code-block:: shell

    python codergpt_cli.py explain -f my_function /path/to/file.py

Add comments to a file with overwrite enabled:

.. code-block:: shell

    python codergpt_cli.py comment --overwrite /path/to/file.py

Optimize a class within a file without overwriting:

.. code-block:: shell

    python codergpt_cli.py optimize -c MyClass /path/to/file.py

Write tests for a function:

.. code-block:: shell

    python codergpt_cli.py write-tests -f my_function /path/to/file.py

Write documentation for a file:

.. code-block:: shell

    python codergpt_cli.py document /path/to/file.py

Parameters and Options
----------------------

-path
  The path to the code file, package, or directory. This is a required argument for all commands.

-f, --function
  The name of the function to explain, optimize, or write tests for. This is an optional argument for the ``explain``, ``optimize``, and ``write-tests`` commands.

-c, --classname
  The name of the class to explain, optimize, or write tests for. This is an optional argument for the ``explain``, ``optimize``, and ``write-tests`` commands.

--overwrite/--no-overwrite
  A flag indicating whether to overwrite the existing file. This is an optional argument for the ``comment`` and ``optimize`` commands.
```