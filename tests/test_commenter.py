"""Test commenter."""

import os
import unittest
from unittest.mock import MagicMock

from codergpt import CodeCommenter

from tests.test_constants import TEST_INPUT_DIR


class TestCodeCommenter(unittest.TestCase):
    """Class for testing the CodeCommenter class."""

    def setUp(self):
        """Set up the test case by creating a mock chain object and initializing the CodeCommenter instance."""
        self.mock_chain = MagicMock()
        self.commenter = CodeCommenter(chain=self.mock_chain)

    def test_comment_with_overwrite(self):
        """Test the comment method with overwrite set to True."""
        # Setup
        code = "print('Hello, World!')"
        filename = TEST_INPUT_DIR / "test.py"
        expected_commented_code = "# This prints a message to the console\nprint('Hello, World!')"

        # Configure the mock to return the expected commented code
        self.mock_chain.invoke.return_value.content = expected_commented_code

        # Act
        self.commenter.comment(code=code, filename=filename, overwrite=True, language="python")

        # Assert
        self.mock_chain.invoke.assert_called_once()
        with open(filename, "r") as f:
            content = f.read()
            self.assertEqual(content, expected_commented_code)

    def test_comment_without_overwrite(self):
        """Test the comment method without overwrite set."""
        # Setup
        code = "print('Goodbye, World!')"
        filename = TEST_INPUT_DIR / "test.py"
        updated_filename = TEST_INPUT_DIR / "test_updated.py"
        expected_commented_code = "# This prints a farewell message to the console\nprint('Goodbye, World!')"

        # Configure the mock to return the expected commented code
        self.mock_chain.invoke.return_value.content = expected_commented_code

        # Act
        self.commenter.comment(code=code, filename=filename)

        # Assert
        self.mock_chain.invoke.assert_called_once()
        with open(updated_filename, "r") as f:
            content = f.read()
            self.assertEqual(content, expected_commented_code)

    def tearDown(self):
        """Clean up created files after each test case."""
        os.remove(TEST_INPUT_DIR / "test.py") if os.path.exists(TEST_INPUT_DIR / "test.py") else None
        os.remove(TEST_INPUT_DIR / "test_updated.py") if os.path.exists(TEST_INPUT_DIR / "test_updated.py") else None


if __name__ == "__main__":
    unittest.main()
