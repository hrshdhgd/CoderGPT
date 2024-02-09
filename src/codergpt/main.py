"""Main python file."""


import os
from pathlib import Path
from typing import Dict, Set, Union

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# Define a function to determine the programming language from a file extension.
def get_language_from_extension(ext: Set[str]) -> Dict[str, str]:
    """Get language from file extension."""
    # Initialize the ChatOpenAI object with an API key from the environment variables.
    llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    # Create a prompt template with predefined messages to set the context for the AI.
    # Here, we tell the AI that it is a "world class software developer".
    prompt = ChatPromptTemplate.from_messages(
        [("system", "You are world class software developer."), ("user", "{input}")]
    )

    # Combine the prompt template with the ChatOpenAI object to create a chain.
    # This chain will be used to send the input to the AI in the correct context.
    chain = prompt | llm

    # Invoke the chain with the specific input asking about the programming language
    # associated with the given file extension. The input is formatted to include the
    # file extension in the question and requests a one-word response.
    response = chain.invoke(
        {
            "input": f"Given the file extensions {ext},\
               return just programming language name e.g. 'Python' or 'JavaScript'."
        }
    )
    return response.content


def inspecting_code(path: Union[str, Path]) -> Dict[str, str]:
    """Inspecting the code and returning a mapping of files to their languages."""
    print("Inspecting the code.")

    # Initialize an empty dictionary to store the results
    file_language_map = {}

    # Convert path to Path object if it's a string
    path = Path(path)

    # Check if the path is a directory or a file
    if path.is_dir():
        # Iterate over all files in the directory and subdirectories
        for file in path.rglob("*.*"):
            language = get_language_from_extension(file.suffix)
            file_language_map[str(file)] = language
    elif path.is_file():
        # Get the language for the single file
        language = get_language_from_extension(path.suffix)
        file_language_map[str(path)] = language
    else:
        print(f"The path {path} is neither a file nor a directory.")
        return file_language_map

    return file_language_map


def start():
    """Entry point function."""
    path = Path("src")
    language_map = inspecting_code(path)
    print(language_map)


if __name__ == "__main__":
    start()
