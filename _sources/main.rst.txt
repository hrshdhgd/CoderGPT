.. automodule:: codergpt
   :members:
   :undoc-members:
   :show-inheritance:

CoderGPT
=======

.. autoclass:: CoderGPT
   :members:
   :undoc-members:
   :show-inheritance:

The ``CoderGPT`` class is designed to integrate various functionalities for working with code files, including inspecting, explaining, commenting, optimizing, testing, and documenting the code. It leverages a language model from OpenAI, specifically GPT-4 Turbo, to perform these tasks.

.. automethod:: __init__

Constructor
-----------

.. automethod:: CoderGPT.__init__

The constructor initializes the ``CoderGPT`` class with a specified model. By default, it uses the GPT-4 Turbo model. It sets up the language model with an API key from the environment variables and constructs a chain of operations starting with a prompt template indicating the role of a world-class software developer.

Inspect Package
---------------

.. automethod:: inspect_package

This method inspects a given package or directory path, identifying the programming language of each file based on its file extension. It displays a table mapping files to their detected languages and returns this mapping as a dictionary.

Get Code
--------

.. automethod:: get_code

Extracts and returns the source code of a specified function or class within a file. If neither a function nor a class is specified, it returns the entire source code of the file.

Explainer
---------

.. automethod:: explainer

Takes a path to a code file and optionally a function or class name, then explains the content or functionality of the specified code. It utilizes a ``CodeExplainer`` instance to perform this explanation.

Commenter
---------

.. automethod:: commenter

Adds comments to a code file at the specified path. It can optionally overwrite existing comments. This is facilitated by a ``CodeCommenter`` instance.

Optimizer
---------

.. automethod:: optimizer

Optimizes the code within a file for performance or readability. The method allows specifying a function or class to focus the optimization on. It leverages a ``CodeOptimizer`` to perform these optimizations.

Test Writer
-----------

.. automethod:: test_writer

Generates tests for a specified function or class within a code file. This functionality is provided through a ``CodeTester`` instance.

Documenter
----------

.. automethod:: documenter

Documents the code in a given file, producing comprehensive documentation that can include descriptions of functionality, parameters, return values, and more. This is accomplished using a ``CodeDocumenter`` instance.

Main
----

The script checks if it is the main module and, if so, creates an instance of ``CoderGPT`` and inspects the "src" directory. This serves as an example of how to use the ``CoderGPT`` class to perform an inspection of a codebase.