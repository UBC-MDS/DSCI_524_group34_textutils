# textutils

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
  Identifies and returns the most frequently occurring word in a string. The function will be case-insensitive and ignore punctuation.

- reverse_text(text: str) -> str
  Reverses the input string and returns the reversed result. The function will validate input types and handle edge cases such as empty strings.

## Relationship to the Python Ecosystem

Python has several powerful text-processing libraries such as:

- [re](https://docs.python.org/3/library/re.html) for regular expressions

- [nltk](https://www.nltk.org/) and [textblob](https://textblob.readthedocs.io/en/dev/) for advanced natural language processing

While these libraries provide extensive functionality, they can be unnecessarily complex for simple text manipulation tasks. textutils is intended to complement existing tools by offering a minimal, lightweight alternative for common text operations that do not require full NLP pipelines.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`textutils` was created by DSCI_524_group34. It is licensed under the terms of the MIT license.

## Credits

`textutils` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
