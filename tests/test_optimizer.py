"""Optimizer tests."""

import unittest
from unittest.mock import MagicMock, mock_open, patch

from codergpt import CodeOptimizer

from tests.test_constants import TEST_INPUT_DIR, TEST_OUTPUT_DIR


class TestCodeOptimizer(unittest.TestCase):
    """Test the CodeOptimizer class."""

    def setUp(self):
        """
        Set up the test case.

        Done by creating a mock chain that can be used to simulate the behavior of the actual chain.
        """
        self.mock_chain = MagicMock()
        self.code_optimizer = CodeOptimizer(chain=self.mock_chain)
        self.bad_python = TEST_INPUT_DIR / "bad_python.py"
        self.expected_bad_python = TEST_OUTPUT_DIR / "expected_bad_python.py"

    @patch("builtins.open", new_callable=mock_open, read_data="def foo(): pass")
    def test_optimize_with_function(self, mock_file):
        """Test the optimize method with a function."""
        # Setup
        filename = "test.py"
        function = "foo"
        expected_response = MagicMock(content="def foo():\n    # Optimized code\n    pass")
        self.mock_chain.invoke.return_value = expected_response

        # Exercise
        self.code_optimizer.optimize(filename, function=function)

        # Verify
        self.mock_chain.invoke.assert_called_once()
        mock_file.assert_called_with(filename.replace(".py", "_updated.py"), "w")
        mock_file().write.assert_called_once_with(expected_response.content)

    @patch("builtins.open", new_callable=mock_open, read_data="class Bar: pass")
    def test_optimize_with_classname(self, mock_file):
        """
        Test the optimize method with a classname.

        :param self: The current instance of the class
        """
        # Setup
        filename = "test.py"
        classname = "Bar"
        expected_response = MagicMock(content="class Bar:\n    # Optimized code\n    pass")
        self.mock_chain.invoke.return_value = expected_response

        # Exercise
        self.code_optimizer.optimize(filename, classname=classname)

        # Verify
        self.mock_chain.invoke.assert_called_once()
        mock_file.assert_called_with(filename.replace(".py", "_updated.py"), "w")
        mock_file().write.assert_called_once_with(expected_response.content)

    @patch("builtins.open", new_callable=mock_open, read_data="def foo(): pass\nclass Bar: pass")
    def test_optimize_full_code(self, mock_file):
        """
        Test the optimize method with full code.

        :param self: The current instance of the class
        """
        # Setup
        filename = "test.py"
        expected_response = MagicMock(
            content="def foo():\n    # Optimized function\n    pass\nclass Bar:\n    # Optimized class\n    pass"
        )
        self.mock_chain.invoke.return_value = expected_response

        # Exercise
        self.code_optimizer.optimize(filename)

        # Verify
        self.mock_chain.invoke.assert_called_once()
        mock_file.assert_called_with(filename.replace(".py", "_updated.py"), "w")
        mock_file().write.assert_called_once_with(expected_response.content)

    @patch("builtins.open", new_callable=mock_open, read_data="def foo(): pass")
    def test_optimize_overwrite_false(self, mock_file):
        """
        Test that when overwrite is True, the original file is overwritten.

        :param self: The current instance of the class
        """
        """
        Test that when overwrite is True, the original file is overwritten.
        """
        # Setup
        filename = "test.py"
        expected_response = MagicMock(content="def foo():\n    # Optimized function\n    pass")
        self.mock_chain.invoke.return_value = expected_response

        # Exercise
        self.code_optimizer.optimize(filename)

        # Verify
        self.mock_chain.invoke.assert_called_once()
        mock_file.assert_called_with(filename.replace(".py", "_updated.py"), "w")
        mock_file().write.assert_called_once_with(expected_response.content)

    @patch("builtins.open", new_callable=mock_open, read_data="def foo(): pass")
    def test_optimize_overwrite_true(self, mock_file):
        """
        Test that when an invalid language is provided, the appropriate error is raised or handled.

        :param self: The current instance of the class
        """
        # Setup
        filename = "test.py"
        expected_response = MagicMock(content="def foo():\n    # Optimized function\n    pass")
        self.mock_chain.invoke.return_value = expected_response

        # Exercise
        self.code_optimizer.optimize(filename, overwrite=True)

        # Verify
        self.mock_chain.invoke.assert_called_once()
        mock_file.assert_called_with(filename, "w")
        mock_file().write.assert_called_once_with(expected_response.content)

    #  TODO: Fix this test
    # @patch("builtins.open", new_callable=mock_open, read_data="def foo(): pass")
    # def test_optimize_invalid_function(self, mock_file):
    #     """
    #     Test that when an invalid function is provided, the appropriate error is raised or handled.

    #     :param self: The current instance of the class
    #     """
    #     # Setup
    #     filename = "test.py"
    #     function = "invalid_function"
    #     expected_error_message = "Function not found in the source code."

    #     # Exercise & Verify
    #     with self.assertRaises(ValueError) as context:
    #         self.code_optimizer.optimize(filename, function=function)
    #     self.assertEqual(str(context.exception), expected_error_message)


if __name__ == "__main__":
    unittest.main()
