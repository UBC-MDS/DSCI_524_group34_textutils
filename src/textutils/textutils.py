"""
This module contains several text utility functions.

Functions:
- word_count(str) -> int: Returns the number of words in the given text.
- remove_punctuation(str) -> str: Removes all punctuation from the given text.
- most_common_word(str) -> str: Returns the most common word in the given text.
- reverse_text(str) -> str: Returns the reversed version of the given text.
"""

def word_count(text):
    """
    Count the number of words in a given text.

    A word is defined as a sequence of characters separated by whitespace.
    Punctuation is treated as part of a word and does not create new words.
    Leading, trailing, and multiple intermediate spaces are handled gracefully.

    Parameters
    ----------
    text : str
        The input text whose words are to be counted.

    Returns
    -------
    int
        The number of words in the input text.

    Raises
    ------
    TypeError
        If the input text is not a string.

    Examples
    --------
    >>> word_count("Hello world")
    2
    >>> word_count("  This   is a test ")
    4
    >>> word_count("")
    0
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    stripped_text = text.strip()
    if stripped_text == "":
        return 0

    words = stripped_text.split()
    return len(words)

def reverse_text(text, mode = 'word'):
    """
    Reverses the given text either by words or by characters.

    Parameters
    ----------
    text : str
        The text to be reversed.
    mode : str, optional
        The mode of reversal. 'word' to reverse by words, 'char' to reverse by characters.
        Default is 'word'.

    Returns
    -------
    str
        The reversed text.

    Raises
    ------
    ValueError
        If the mode is not 'word' or 'char'.
    TypeError
        If the input text is not a string.

    Examples
    --------
    >>> reverse_text('Hello World', mode = 'word')
    'World Hello'
    >>> reverse_text('Hello World', mode = 'char')
    'dlroW olleH'
    """
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    if mode == 'word':
        words = text.split()
        return ' '.join(reversed(words))
    elif mode == 'char':
        return text[::-1]
    else:
        raise ValueError('Mode must be either \'word\' or \'char\'')


def most_common_word(text, case_sensitive=False):
    """
    Identify the most common word in a given text.

    Parameters
    ----------
    text : str
        The text to find the most common word of.
    case_sensitive: bool, optional
        Switch to identify the most common word based on case-sensitive/insensitive.
        Default is False (case-insensitive).

    Returns
    -------
    str
        The most common word in the given text.

    Raises
    ------
    TypeError
        If the input text is not a string.

    Examples
    --------
    >>> most_common_word("Hello. Hello. hello. How's your day?")
    'hello'
    >>> most_common_word("Hello. Hello. hello. How's your day?", True)
    'Hello'
    """
    
    # if the input is not str type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    # if the input is empty
    if text == "":
        return ""
    # remove punctuation
    text = remove_punctuation(text)
    # change to lower case if user wants to count based on case-insensitive
    if not case_sensitive:
        text = text.lower()
    # split the word by spaces
    words = text.split()
    # return "" if no words left after removing punctuation and spaces
    if not words:
        return ""
    # create dict to keep track of word:word_count
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1

    most_common = words[0]
    max_count = counter[most_common]

    for w in counter:
        if counter[w] > max_count:
            most_common = w
            max_count = counter[w]

    return most_common


def remove_punctuation(text):
    """
    Remove all punctuation from the given text.

    Parameters
    ----------
    text : str
        The text from which to remove punctuation.

    Returns
    -------
    str
        The text with all punctuation removed.

    Raises
    ------
    TypeError
        If the input text is not a string.

    Examples
    --------
    >>> remove_punctuation('Hello, World!')
    'Hello World'
    >>> remove_punctuation('What?! No way...')
    'What No way'
    >>> remove_punctuation('')
    ''
    >>> remove_punctuation('Numbers 123 are fine!')
    'Numbers 123 are fine'
    >>> remove_punctuation('Emojis 😀 stay too!')
    'Emojis 😀 stay too'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    import string
    return text.translate(str.maketrans("", "", string.punctuation))
