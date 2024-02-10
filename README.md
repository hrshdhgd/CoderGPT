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

#### inspect

Inspect a package and display a file-language map.

```shell
code inspect <path>
```

##### example
```shell
code inspect code inspect src/codergpt/
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


#### explain

Explain a specific function or class within a package.

```shell
code explain <path> [--function <function_name>] [--classname <class_name>]
```

#### comment

Add comments to the code in a package.

```shell
code comment <path> [--overwrite/--no-overwrite]
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

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).

For more information on CoderGPT CLI, please visit [the official documentation]().
