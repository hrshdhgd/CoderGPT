"""Tests for the CodeTester class."""

import os
import unittest
from pathlib import Path

from codergpt.test_writer.test_writer import CodeTester
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from .test_constants import TEST_INPUT_DIR, TEST_OUTPUT_DIR


class CodeTesterTests(unittest.TestCase):
    """Tests for the CodeTester class."""

    def setUp(self):
        """Create a sample runnable chain for testing."""
        self.llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", "You are world class software developer."), ("user", "{input}")]
        )
        self.chain = self.prompt | self.llm
        self.code_tester = CodeTester(chain=self.chain)
        self.filename = TEST_INPUT_DIR / "math.py"
        self.output_filename = TEST_OUTPUT_DIR / "test_math.py"

    def tearDown(self):
        """Clean up the created test files."""
        test_files = Path(TEST_OUTPUT_DIR).glob("test_*")
        for file in test_files:
            file.unlink()

    @unittest.skipIf(os.getenv("GITHUB_ACTIONS") == "true", "Skipping tests in GitHub Actions")
    def test_write_tests_with_function(self):
        """Test writing tests for a function."""
        # Arrange
        function = "calculate_sum"

        # Act
        outfile = TEST_OUTPUT_DIR / "test_math_function.py"
        self.code_tester.write_tests(self.filename, function=function, outfile=outfile)

        self.assertTrue(outfile.exists())

    @unittest.skipIf(os.getenv("GITHUB_ACTIONS") == "true", "Skipping tests in GitHub Actions")
    def test_write_tests_with_class(self):
        """Test writing tests for a class."""
        # Arrange
        classname = "MathOperations"

        # Act
        outfile = TEST_OUTPUT_DIR / "test_math_class.py"
        self.code_tester.write_tests(self.filename, classname=classname, outfile=outfile)

        self.assertTrue(outfile.exists())

    @unittest.skipIf(os.getenv("GITHUB_ACTIONS") == "true", "Skipping tests in GitHub Actions")
    def test_write_tests_without_function_or_class(self):
        """Test writing tests for a file."""
        # Act
        outfile = self.output_filename
        self.code_tester.write_tests(self.filename, outfile=outfile)
        self.assertTrue(outfile.exists())


if __name__ == "__main__":
    unittest.main()
