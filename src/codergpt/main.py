"""Main python file."""

import os
from pathlib import Path
from typing import Dict, Union

import yaml
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from codergpt.constants import EXTENSION_MAP_FILE


class CoderGPT:
    """CoderGPT class."""

    def __init__(self):
        """Initialize the CoderGPT class."""
        # Initialize the ChatOpenAI object with an API key from the environment variables.
        self.llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
        # Create a prompt template with predefined messages to set the context for the AI.
        # Here, we tell the AI that it is a "world class software developer".
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", "You are world class software developer."), ("user", "{input}")]
        )
        # Combine the prompt template with the ChatOpenAI object to create a chain.
        # This chain will be used to send the input to the AI in the correct context.
        self.chain = self.prompt | self.llm

        # # Invoke the chain with the specific input asking about the programming language
        # # associated with the given file extension. The input is formatted to include the
        # # file extension in the question and requests a one-word response.
        # response = chain.invoke(
        #     {
        #         "input": f"Given the file extensions {ext},\
        #         return just programming language name e.g. 'Python' or 'JavaScript'."
        #     }
        # )

    def inspect_package(self, path: Union[str, Path]) -> Dict[str, str]:
        """Inspecting the code and returning a mapping of files to their languages."""
        print("Inspecting the code.")

        with open(EXTENSION_MAP_FILE, "r") as file:
            extension_to_language = yaml.safe_load(file)

        # Initialize an empty dictionary to store the results
        file_language_map = {}

        # Convert path to Path object if it's a string
        path = Path(path)

        # Check if the path is a directory or a file
        if path.is_dir():
            # Iterate over all files in the directory and subdirectories
            file_language_map = {
                str(file): extension_to_language["language-map"].get(file.suffix)
                for file in path.rglob("*.*")
                if extension_to_language["language-map"].get(file.suffix) is not None
            }

        elif path.is_file():
            # Get the language for the single file
            language = extension_to_language["language-map"].get(path.suffix)
            if language is not None:
                file_language_map[str(path)] = language

        else:
            print(f"The path {path} is neither a file nor a directory.")
            return file_language_map
        return file_language_map


if __name__ == "__main__":
    coder = CoderGPT()
    coder.inspect_package("src")
