"""
This module contains several text utility functions.

Functions:
- word_count(str) -> int: Returns the number of words in the given text.
- remove_punctuation(str) -> str: Removes all punctuation from the given text.
- most_common_word(str) -> str: Returns the most common word in the given text.
- reverse_text(str) -> str: Returns the reversed version of the given text.
"""

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
    pass

