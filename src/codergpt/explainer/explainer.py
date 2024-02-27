"""Explainer Module."""

from typing import Any, Dict, Optional

from langchain_core.runnables.base import RunnableSerializable


class CodeExplainer:
    """Code Explainer class that extracts and explains code from a given file."""

    def __init__(self, chain: RunnableSerializable[Dict, Any]):
        """
        Initialize the CodeExplainer class with a runnable chain.

        :param chain: A RunnableSerializable object capable of executing tasks.
        """
        self.chain = chain

    def explain(
        self, code: str, function: Optional[str] = None, classname: Optional[str] = None, language: Optional[str] = None
    ):
        """
        Explain the contents of the code file by invoking the runnable chain.

        :param code: The code to be explained.
        :param function: The name of the function to explain. Default is None.
        :param classname: The name of the class to explain. Default is None.
        """
        if function:
            response = self.chain.invoke(
                {"input": f"Explain the function {function} in the following {language} code: \n\n```\n{code}\n```"}
            )
            # Pretty print the response
            print(f"Explanation for '{function}':\n{response.content}")
        elif classname:
            response = self.chain.invoke(
                {"input": f"Explain the class {classname} in the following {language} code: \n\n```\n{code}\n```"}
            )
            # Pretty print the response
            print(f"Explanation for '{classname}':\n{response.content}")
        else:
            # Explain full code
            response = self.chain.invoke({"input": f"Explain the following {language} code: \n\n```\n{code}\n```"})
            # Pretty print the response
            print(f"Explanation for the code:\n{response.content}")
