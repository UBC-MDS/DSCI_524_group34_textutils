"""
Unit tests for the word_count function.

These tests verify that word_count correctly counts the number of words
in a string under normal conditions, handles edge cases such as empty
or whitespace-only strings, and raises appropriate errors for invalid input.
"""

import pytest
from textutils.textutils import word_count


def test_word_count_normal_sentence():
    """
    Test that word_count correctly counts words in a simple sentence
    with single spaces between words.
    """
    assert word_count("Hello world") == 2


def test_word_count_extra_spaces():
    """
    Test that word_count correctly handles leading, trailing,
    and multiple intermediate spaces.
    """
    assert word_count("  This   is a test ") == 4


def test_word_count_empty_string():
    """
    Test that word_count returns 0 for an empty string.
    """
    assert word_count("") == 0


def test_word_count_only_whitespace():
    """
    Test that word_count returns 0 for a string containing
    only whitespace characters.
    """
    assert word_count("     ") == 0


def test_word_count_with_punctuation():
    """
    Test that punctuation is treated as part of a word and
    does not affect the word count.
    """
    assert word_count("Hello, world!") == 2


def test_word_count_non_string_input():
    """
    Test that word_count raises a TypeError when the input
    is not a string.
    """
    with pytest.raises(TypeError, match="Input text must be a string"):
        word_count(123)
