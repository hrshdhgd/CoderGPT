"""
Tests for the CodeDocumenter class.

This module contains test cases for testing
the functionality of the CodeDocumenter class, ensuring it behaves as expected
under various conditions.

.. module:: test_documenter
   :synopsis: Tests for the CodeDocumenter class.
"""

import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from codergpt.constants import DOCS_DIR
from codergpt.documenter import CodeDocumenter


class TestCodeDocumenter(unittest.TestCase):
    """
    Test suite for the CodeDocumenter class.

    This class contains setup methods and test cases to validate the
    functionality of the CodeDocumenter class.
    """

    def setUp(self):
        """
        Set up method to prepare the test fixture before each test method.

        This method is called before each individual test function, and it
        initializes a mock chain and a CodeDocumenter instance to be used
        across different test cases.
        """
        self.mock_chain = Mock()
        self.documenter = CodeDocumenter(chain=self.mock_chain)

    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="def example():\n    pass")
    def test_document_with_mock_chain(self, mock_open):
        """
        Test the document method with a mocked chain.

        This test case checks if the document method correctly interacts with
        the provided mock objects when documenting code with a specified output
        file.

        :param mock_open: A mock object for the open function.
        :type mock_open: unittest.mock.MagicMock
        """
        # Setup
        filename = "example.py"
        outfile = "output.rst"
        self.mock_chain.invoke.return_value = Mock(content="Documented content")

        # Execute
        self.documenter.document(filename, outfile)

        # Assert
        self.mock_chain.invoke.assert_called_once()
        mock_open.assert_called_with(outfile, "w")
        mock_open().write.assert_called_once_with("Documented content")

    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="def example():\n    pass")
    def test_document_without_outfile(self, mock_open):
        """
        Test the document method without specifying an output file.

        This test case checks if the document method correctly handles the
        case where no output file is specified, defaulting to saving the
        document in the DOCS_DIR directory.

        :param mock_open: A mock object for the open function.
        :type mock_open: unittest.mock.MagicMock
        """
        # Setup
        filename = "example.py"
        self.mock_chain.invoke.return_value = Mock(content="Documented content")

        # Execute
        self.documenter.document(filename)

        # Assert
        expected_path = DOCS_DIR / "example.rst"
        mock_open.assert_called_with(expected_path, "w")
        mock_open().write.assert_called_once_with("Documented content")

    def test_document_with_pathlib_path(self):
        """
        Test the document method with a Pathlib path as input.

        This test case verifies that the document method correctly handles
        input filenames provided as Pathlib Path objects, documenting the code
        with a specified output file.

        The open function is patched and spied on to ensure the file operations
        are performed as expected.
        """
        # Setup
        filename = Path("example.py")
        outfile = "output.rst"
        self.mock_chain.invoke.return_value = Mock(content="Documented content")

        # Patch and Spy
        with patch("builtins.open", unittest.mock.mock_open()) as mock_open:
            self.documenter.document(filename, outfile)

            # Assert
            self.mock_chain.invoke.assert_called_once()
            mock_open.assert_called_with(outfile, "w")
            mock_open().write.assert_called_once_with("Documented content")


if __name__ == "__main__":
    unittest.main()
