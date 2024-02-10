# CoderGPT CLI

## Description

CoderGPT CLI is a command line interface, a state-of-the-art code generation/modifying tool. It allows developers to interact with the CoderGPT functionalities directly from the terminal, streamlining their workflow and enhancing productivity. The underlying engine that facilitates the code enhancement and modificatoin is [langchain](https://github.com/langchain-ai/langchain).

## Author

Harshad Hegde

## Installation

To use the CoderGPT CLI, clone the repository and install the required dependencies.

```shell
pip install codergpt
```

## Usage

Run the CLI using the following syntax:

```shell
code [OPTIONS] COMMAND [ARGS]...
```

### Options

- `-v, --verbose INTEGER`: Set verbosity level (0, 1, or 2).
- `-q, --quiet`: Enable quiet mode.
- `--version`: Display version information.

### Commands

1. `inspect`: Inspect a package and display a file-language map.


    ```shell
    code inspect <path>
    ```

    #### Example
    ```shell
    $ code inspect code inspect src/codergpt/
    Inspecting the code.
    File                                        Language
    ------------------------------------------  ----------
    src/codergpt/constants.py                   Python
    src/codergpt/__init__.py                    Python
    src/codergpt/cli.py                         Python
    src/codergpt/extensions.yaml                YAML
    src/codergpt/main.py                        Python
    src/codergpt/optimizer/__init__.py          Python
    src/codergpt/utils/expression_evaluator.py  Python
    src/codergpt/utils/__init__.py              Python
    src/codergpt/commenter/commenter.py         Python
    src/codergpt/commenter/__init__.py          Python
    src/codergpt/explainer/explainer.py         Python
    src/codergpt/explainer/__init__.py          Python
    src/codergpt/test_writer/__init__.py        Python
    ```


2. `explain`: Explain a specific function or class within a package.

    ```shell
    code explain <path> [--function <function_name>] [--classname <class_name>]
    ```

    #### Example
    ```shell
    $ code explain src/codergpt/explainer/explainer.py --function explain
    Explanation for the code:
    This code defines a method called `explain` that takes in three parameters: `code`, `function`, and `classname`. The `code` parameter is a string that represents the code file to be explained. The `function` parameter is an optional string that represents the name of a specific function within the code file that needs to be explained. The `classname` parameter is also an optional string that represents the name of a specific class within the code file that needs to be explained.

    The method first checks if the `function` parameter is provided. If it is, the method invokes a `chain` by passing a dictionary with an "input" key and a formatted string containing the code. The response from the `chain.invoke` call is then printed in a pretty format, including the name of the function being explained.

    If the `function` parameter is not provided but the `classname` parameter is, the same process is followed, but with the class name instead.

    If both `function` and `classname` parameters are not provided, the method assumes that the full code needs to be explained. It again invokes the `chain` with the code as input and prints the response in a pretty format, indicating that it is explaining the entire code.
    ```

3. `comment`: Add comments to the code in a package. The user has the choice to overwrite the file or create a new one.

    ```shell
    code comment <path> [--overwrite/--no-overwrite]
    ```
    #### Example
    - Let's consider a python file `greetings.py`:
    ```
        def greet(name):
            return f"Hello, {name}!"

        if __name__ == "__main__":
            user_name = "Alice"
            print(greet(user_name))
    ```

    ```shell
    $ code comment greetings.py --overwrite
    ```
    results in .... 
    ```
        def greet(name):
            """
            Generates a greeting message for the given name.

            :param name: (str) The name of the person to greet.
            :return: (str) The greeting message.
            """
            return f"Hello, {name}!"


        if __name__ == "__main__":
            user_name = "Alice"
            print(greet(user_name))
    ```
## Development

The CLI is built using Python and the `click` library. Below is an example of how to define a new command:

```python
import click
from codergpt import CoderGPT

coder = CoderGPT()

@click.command()
@click.argument('path', type=click.Path(exists=True))
def new_command(path):
    # Command logic here
    pass
```

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).

For more information on CoderGPT CLI, please visit [the official documentation]().
