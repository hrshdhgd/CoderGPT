"""Test explainer."""

import unittest
from unittest.mock import Mock

from codergpt import CodeExplainer

sample_code = "def sample_function():\n    pass"
sample_function_name = "sample_function"
sample_class_name = "SampleClass"

mock_response = Mock()
mock_response.content = "This is a mock explanation."


class TestExplainer(unittest.TestCase):
    """Test Explainer Class."""

    def setUp(self):
        """Set up for creating a mock chain object and CodeExplainer object."""
        self.mock_chain = Mock()
        self.mock_response = Mock()
        self.mock_response.content = "Mocked explanation content"
        self.mock_chain.invoke.return_value = self.mock_response
        self.code_explainer = CodeExplainer(chain=self.mock_chain)

    def test_explain_function(self):
        """Test case for explaining a function."""
        sample_code = "def example(): pass"  # Replace with actual code
        sample_function_name = "example"  # Replace with actual function name

        # Call the explain method with a sample code snippet and function name
        self.code_explainer.explain(code=sample_code, function=sample_function_name, language="python")

        # Verify that invoke was called once with the correct parameters
        expected_invoke_input = {
            "input": f"Explain the function {sample_function_name} "
            f"in the following python code: \n\n```\n{sample_code}\n```"
        }
        self.mock_chain.invoke.assert_called_once_with(expected_invoke_input)

        # Check if the expected explanation message is in the captured output
        # This assumes that CodeExplainer prints the explanation to stdout
        captured_out = self.mock_chain.invoke.return_value.content
        expected_output = f"Explanation for '{sample_function_name}':\n{self.mock_response.content}"
        self.assertIn(captured_out, expected_output)

    def test_explain_class(self):
        """Test case for explaining a class."""
        sample_code = "class Example: pass"  # Replace with actual code
        sample_class_name = "Example"  # Replace with actual class name

        # Call the explain method with a sample code snippet and class name
        self.code_explainer.explain(code=sample_code, classname=sample_class_name, language="python")

        # Verify that invoke was called once with the correct parameters
        expected_invoke_input = {
            "input": f"Explain the class {sample_class_name} in the following python code: \n\n```\n{sample_code}\n```"
        }
        self.mock_chain.invoke.assert_called_once_with(expected_invoke_input)

        # Check if the expected explanation message is in the captured output
        captured_out = self.mock_chain.invoke.return_value.content
        expected_output = f"Explanation for '{sample_class_name}':\n{self.mock_response.content}"
        self.assertIn(captured_out, expected_output)

    def test_explain_full_code(self):
        """Test case for explaining full code."""
        sample_code = "# Your full code here"  # Replace with actual code

        # Call the explain method with a sample code snippet
        self.code_explainer.explain(code=sample_code, language="python")

        # Verify that invoke was called once with the correct parameters
        expected_invoke_input = {"input": f"Explain the following python code: \n\n```\n{sample_code}\n```"}
        self.mock_chain.invoke.assert_called_once_with(expected_invoke_input)

        # Check if the expected explanation message is in the captured output
        captured_out = self.mock_chain.invoke.return_value.content
        expected_output = "Explanation for the code:\nMocked explanation content."
        self.assertIn(captured_out, expected_output)
