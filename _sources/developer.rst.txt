.. _developer-docs:

Developer Documentation
========================

This section contains documentation for developers who want to contribute or extend the functionality of the project.


Command Line Interface for CoderGPT
===================================

Overview
--------

This module provides a command line interface (CLI) for CoderGPT, a powerful code generation tool that facilitates various operations on code files such as inspection, explanation, commenting, and optimization.

Usage
-----

To use the CLI, run the following command with the desired options and commands:

.. code-block:: shell

    python codergpt_cli.py [OPTIONS] COMMAND [ARGS]...

Options
-------

-v, --verbose INTEGER
  Verbosity level (0, 1 or 2).

-q, --quiet
  Run in quiet mode.

--version
  Show the version and exit.

Commands
--------

inspect
  Inspect package to show file-language-map.

explain
  Explain the contents of a code file.

comment
  Add comments to a code file.

Details
-------

The CLI is built using the Click library and provides a user-friendly way to interact with the CoderGPT functionalities from the terminal.

Examples
--------

Inspecting a package:

.. code-block:: shell

    python codergpt_cli.py inspect src/

Explaining a function within a file:

.. code-block:: shell

    python codergpt_cli.py explain src/main.py --function my_function

Adding comments to a file:

.. code-block:: shell

    python codergpt_cli.py comment src/main.py --overwrite

Optimizing a class within a file:

.. code-block:: shell

    python codergpt_cli.py optimize src/main.py --classname MyClass --overwrite

Environment Variables
---------------------

- ``OPENAI_API_KEY``: The API key for OpenAI services required by CoderGPT.

Dependencies
------------

- click
- logging
- pathlib.Path
- typing.TextIO, typing.Union
- codergpt.__version__
- codergpt.main.CoderGPT


Main Python File
================

This is the main Python file for the CoderGPT project.

Classes
-------

.. autoclass:: CoderGPT
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__
   .. automethod:: inspect_package
   .. automethod:: get_code
   .. automethod:: explainer
   .. automethod:: commenter
   .. automethod:: optimizer
   .. automethod:: tester

Description
-----------

The ``CoderGPT`` class provides a suite of methods to interact with code files, including inspection, explanation, commenting, optimization, and testing. It utilizes language models to perform these tasks.

Dependencies
------------

- os
- pathlib.Path
- typing.Optional, typing.Union
- yaml
- langchain_core.prompts.ChatPromptTemplate
- langchain_openai.ChatOpenAI
- tabulate.tabulate
- codergpt.commenter.commenter.CodeCommenter
- codergpt.constants.EXTENSION_MAP_FILE, codergpt.constants.GPT_3_5_TURBO, codergpt.constants.INSPECTION_HEADERS
- codergpt.explainer.explainer.CodeExplainer
- codergpt.optimizer.optimizer.CodeOptimizer

Usage
-----

To use the ``CoderGPT`` class, initialize it with an optional model parameter. Then call its methods with appropriate arguments to perform various operations on code files.

Example:

.. code-block:: python

    if __name__ == "__main__":
        coder = CoderGPT()
        coder.inspect_package("src")

Environment Variables
---------------------

- ``OPENAI_API_KEY``: The API key for OpenAI services.

Files
-----

- ``EXTENSION_MAP_FILE``: YAML file mapping file extensions to programming languages.
