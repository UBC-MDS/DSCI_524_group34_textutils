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


   Examples
   --------
   >>> most_common_word('Hello. Hello. hello. How's your day?')
   'hello'
   >>> most_common_word('Hello. Hello. hello. How's your day?', True)
   'Hello'
   """
   pass


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
    pass
