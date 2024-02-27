"""BugFinder test cases."""

import os
import unittest
from unittest.mock import patch

from codergpt.bug_finder import BugFinder
from codergpt.constants import TEST_DIR
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class TestBugFinder(unittest.TestCase):
    """Test cases for the BugFinder class."""

    @patch("langchain_core.runnables.base.RunnableSerializable")
    def setUp(self, mock_runnable):
        """Set up method for the test cases."""
        self.bug_finder = BugFinder(mock_runnable)
        self.mock_runnable = mock_runnable

    def test_find_bugs_function(self):
        """Test case for the find_bugs method when the input is a function."""
        code = "def test():\n    pass"
        function = "test"
        language = "python"
        self.bug_finder.find_bugs(code, function=function, language=language)
        self.mock_runnable.invoke.assert_called_once()

    def test_find_bugs_class(self):
        """Test case for the find_bugs method when the input is a class."""
        code = "class Test:\n    pass"
        classname = "Test"
        language = "python"
        self.bug_finder.find_bugs(code, classname=classname, language=language)
        self.mock_runnable.invoke.assert_called_once()

    def test_find_bugs_code(self):
        """Test case for the find_bugs method when the input is a code snippet."""
        code = "print('Hello, World!')"
        language = "python"
        self.bug_finder.find_bugs(code, language=language)
        self.mock_runnable.invoke.assert_called_once()

    def test_fix_bugs_function(self):
        """Test case for the fix_bugs method when the input is a function."""
        code = "def test():\n    pass"
        function = "test"
        language = "python"
        self.bug_finder.fix_bugs("test.py", code, function=function, language=language)
        self.mock_runnable.invoke.assert_called_once()

    def test_fix_bugs_class(self):
        """Test case for the fix_bugs method when the input is a class."""
        code = "class Test:\n    pass"
        classname = "Test"
        language = "python"
        self.bug_finder.fix_bugs("test.py", code, classname=classname, language=language)
        self.mock_runnable.invoke.assert_called_once()

    def test_fix_bugs_code(self):
        """Test case for the fix_bugs method when the input is a code snippet."""
        code = "print('Hello, World!')"
        language = "Python"
        file = TEST_DIR / "input/buggy_code.py"
        llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"), temperature=0.3, model="gpt-3.5-turbo")
        prompt = ChatPromptTemplate.from_messages(
            [("system", "You are world class software developer."), ("user", "{input}")]
        )
        chain = prompt | llm
        actual_bugfinder = BugFinder(
            chain=chain,
        )
        actual_bugfinder.fix_bugs(file, code, language=language, outfile=TEST_DIR / "output/fixed_code.py")
        self.assertTrue((TEST_DIR / "output/fixed_code.py").exists())
        # cleanup
        os.remove(TEST_DIR / "output/fixed_code.py")


if __name__ == "__main__":
    unittest.main()
