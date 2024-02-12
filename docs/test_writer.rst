Test Writing Module
===================

This module contains the ``CodeTester`` class, which is designed to automatically generate and write test cases for given source code files. It uses a runnable chain to generate tests for either specific functions, classes, or entire code files.

Classes
-------

.. autoclass:: CodeTester
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__
   .. automethod:: write_tests

CodeTester
----------

.. py:class:: CodeTester(chain)

   The ``CodeTester`` class is responsible for initializing with a runnable chain and writing tests for code.

   .. py:method:: __init__(chain: RunnableSerializable[Dict, Any])

      Initializes the ``CodeTester`` class with a runnable chain.

      :param chain: A ``RunnableSerializable`` object capable of executing tasks.

   .. py:method:: write_tests(filename: Union[str, Path], function: Optional[str] = None, classname: Optional[str] = None, outfile: Optional[str] = None)

      Writes tests for the code specified in the given file by invoking the runnable chain. The tests can be generated for a specific function, class, or the entire file. The generated test code is then written to an output file.

      :param filename: The path to the code file for which tests are to be generated.
      :param function: (Optional) The name of the function within the file to generate tests for. Default is None, indicating that tests should not be limited to a specific function.
      :param classname: (Optional) The name of the class within the file to generate tests for. Default is None, indicating that tests should not be limited to a specific class.
      :param outfile: (Optional) The path to the output file where the generated test code should be written. If not specified, tests are written to a default directory with a filename prefixed with ``test_``.

