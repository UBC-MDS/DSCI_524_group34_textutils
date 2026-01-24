# Welcome to textutils

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/textutils.svg)](https://pypi.org/project/textutils/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/textutils.svg)](https://pypi.org/project/textutils/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

textutils is a lightweight Python package that provides a small collection of utility functions for basic text processing and manipulation. The package is designed to be simple, beginner-friendly, and easy to integrate into data analysis or general Python workflows where quick text operations are needed without the overhead of large NLP libraries.

## Contributors
- Mehmet Imga
- Shi Fan Jin
- Aidan Hew
- Sidharth Malik

## Installation

```bash
$ pip install textutils
```

## Package Overview

This package will include the following functions:
- word_count(text: str) -> int
  Counts the number of words in a given string. The function will handle empty strings and raise appropriate errors for invalid inputs.

- remove_punctuation(text: str) -> str
  Removes punctuation characters from a string and returns the cleaned text while preserving spacing and alphanumeric characters.

- most_common_word(text: str) -> str
  Identifies and returns the most frequently occurring word in a string. The function ignores punctuation and can be case-insensitive or case-sensitive.

- reverse_text(text: str) -> str
  Reverses the input string and returns the reversed result. The function will validate input types and handle edge cases such as empty strings.

## Quick Usage Examples

```python
from textutils.textutils import (
    word_count,
    remove_punctuation,
    most_common_word,
    reverse_text,
)

word_count("Hello world!")  # returns 2
remove_punctuation("Hello, world!")  # returns "Hello world"
most_common_word("apple banana apple orange")  # returns "apple"
reverse_text("textutils")  # returns "slitxet"

```

## Development Setup

To set up the development environment locally using conda:

1. Clone the repository:

```bash
  git clone https://github.com/UBC-MDS/DSCI_524_group34_textutils.git
  cd DSCI_524_group34_textutils
```

2. Create and activate the conda environment:
   
```bash
  conda env create -f environment.yml
  conda activate textutils
```

3. Install the package in editable mode:

```bash
  pip install -e .
```

## Running Tests

To run the full test suite locally:

```bash
  pytest
```

## Documentation

Package documentation is generated using quartodoc and deployed automatically to GitHub Pages via GitHub Actions.

To build the documentation locally:

```bash
  quarto render docs
```

The deployed documentation can be found at:
https://ubc-mds.github.io/DSCI_524_group34_textutils/

## Relationship to the Python Ecosystem

Python has several powerful text-processing libraries such as:

- [re](https://docs.python.org/3/library/re.html) for regular expressions

- [nltk](https://www.nltk.org/) and [textblob](https://textblob.readthedocs.io/en/dev/) for advanced natural language processing

While these libraries provide extensive functionality, they can be unnecessarily complex for simple text manipulation tasks. textutils is intended to complement existing tools by offering a minimal, lightweight alternative for common text operations that do not require full NLP pipelines.

## Continuous Integration and Deployment

This project uses GitHub Actions for:

- Continuous integration (running tests and style checks on pushes and pull requests)

- Continuous deployment to TestPyPI on pushes to the main branch

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Copyright

- Copyright © 2026 DSCI_524_group34.
- Free software distributed under the [MIT License](./LICENSE).
