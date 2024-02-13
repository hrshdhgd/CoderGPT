# CoderGPT

CoderGPT is a versatile command-line interface (CLI) designed to enhance coding workflows. It leverages the capabilities of Large Language Models (LLM) and Generative Pre-trained Transformers (GPT) to assist developers in various tasks such as commenting, optimizing, documenting, and testing their code. This tool integrates seamlessly with [langchain](https://github.com/langchain-ai/langchain), providing a powerful backend for code generation and modification.

# Model Providers Implemented
 - [x] OpenAI [`gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo-preview`(default)]
 - [x] Google [`gemini-pro`]
 - [ ] Anthropic [`Claude`] (coming soon!)

## Prerequisites

Before you begin using CoderGPT, you must set the `OPENAI_API_KEY` and `GOOGLE_API_KEY` environment variables on your machine. This key enables authentication with the OpenAI and Google APIs, which are essential for the language model's operation.

```sh
export OPENAI_API_KEY='your-api-key-here'
export GOOGLE_API_KEY='your-api-key-here'
```

Ensure that you replace `your-api-key-here` with your actual OpenAI API key to enable the full functionality of CoderGPT.

## Getting Started

### Installation

Install CoderGPT easily using pip:

```shell
pip install codergpt
```

### Basic Usage

Invoke the CoderGPT CLI with the following syntax:

```shell
codergpt [OPTIONS] COMMAND [ARGS]...
```

#### Options

- `-v, --verbose INTEGER`: Adjust the verbosity level (0 for default, 1 for verbose, 2 for debug).
- `-q, --quiet`: Suppress output.
- `--version`: Show the version number and exit.

#### Commands

##### Inspect

Analyze a package and display its file-language mapping.

```shell
codergpt inspect <path>
```

###### Example

```shell
$ codergpt inspect src/codergpt/
```

##### Explain

Provide an explanation for a specific function or class within a package.

```shell
codergpt explain <path> [--function <function_name>] [--classname <class_name>]
```

###### Example

```shell
$ codergpt explain src/codergpt/explainer/explainer.py --function explain
```

##### Comment

Automatically add comments to your code. Choose whether to overwrite the existing file or create a new one.

```shell
codergpt comment <path> [--overwrite/--no-overwrite]
```

###### Example

```shell
$ codergpt comment greetings.py --overwrite
```

##### Optimize

Enhance your code by optimizing it and adding comments. You can decide to overwrite the original file or save the changes separately.

```shell
codergpt optimize <path> [--overwrite/--no-overwrite]
```

###### Example

```shell
$ codergpt optimize example.py --overwrite
```

##### Write Tests

Generate test cases for a specified code file, targeting particular functions and/or classes.

```shell
codergpt write-tests <filename> [--function <function_name>] [--class <classname>] [--outfile <output_filename>]
```

###### Example

```shell
$ codergpt write-tests example.py --function add --class Calculator
```

##### Document

Create documentation for a given code file by processing and explaining the code.

```shell
codergpt document <path> [--outfile <output_filename>]
```

###### Example

```shell
$ codergpt document example.py
```

## Development & Contribution

The CoderGPT CLI is developed in Python, utilizing the `click` library for creating commands. Here's a template for adding a new command:

```python
import click
from codergpt import CoderGPT

coder = CoderGPT()

@click.command()
@click.argument('path', type=click.Path(exists=True))
def new_command(path):
    # Implement command logic here
    pass
```

Contributions to CoderGPT are highly encouraged! Please review our [contributing guidelines](CONTRIBUTING.md) before making pull requests.

## License

CoderGPT is open-sourced under the MIT License. For more details, refer to the [LICENSE.md](LICENSE.md) file.

## Acknowledgments

This project was scaffolded using the [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) framework, based on the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template). Updates are managed through [cruft](https://cruft.github.io/cruft/).

For comprehensive details on the CoderGPT CLI, please refer to [the official documentation](https://hrshdhgd.github.io/CoderGPT/).

---