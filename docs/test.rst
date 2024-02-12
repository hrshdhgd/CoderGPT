.. py:module:: codergpt

Test writing module
===================

.. py:class:: CodeTester(chain)

   The CodeTester class is responsible for generating testing code from a given source file. It utilizes a llm chain to produce tests for specific functions or classes within the source file.

   .. py:method:: __init__(chain)

      Initializes the CodeTester instance with a provided llm chain.

      :param chain: A RunnableSerializable object capable of executing tasks.
      :type chain: RunnableSerializable[Dict, Any]

   .. py:method:: write_tests(filename, function=None, classname=None, outfile=None)

      Generates test cases for the specified code by invoking the llm chain. If a function or class name is provided, it will generate tests specifically for that function or class. Otherwise, it will attempt to create tests for the entire code.

      :param filename: The path to the code file for which tests are to be written.
      :type filename: Union[str, Path]
      :param function: The name of the function for which tests should be generated. Defaults to None, indicating that no specific function is targeted.
      :type function: Optional[str]
      :param classname: The name of the class for which tests should be generated. Defaults to None, indicating that no specific class is targeted.
      :type classname: Optional[str]
      :param outfile: The path where the generated test file should be saved. If not provided, a default path within the TEST_DIR will be used.
      :type outfile: Optional[str]

      The method reads the source code from the provided filename and uses the llm chain to generate appropriate test cases. The resulting test code is then written to either the specified outfile or a new file within the TEST_DIR directory.
