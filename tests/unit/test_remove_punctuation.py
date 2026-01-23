"""
Unit tests for the remove_punctuation function.

Tests cover basic functionality, edge cases, and error handling.
"""

import pytest
from textutils.textutils import remove_punctuation


def test_remove_punctuation_basic():
    """Test basic punctuation removal from a simple sentence."""
    assert remove_punctuation("Hello, World!") == "Hello World"


def test_remove_punctuation_multiple_punctuation():
    """Test removal of multiple consecutive punctuation marks."""
    assert remove_punctuation("What?! No way...") == "What No way"


def test_remove_punctuation_empty_string():
    """Test that empty string returns empty string."""
    assert remove_punctuation("") == ""


def test_remove_punctuation_numbers_preserved():
    """Test that numbers are preserved in the output."""
    assert remove_punctuation("Numbers 123 are fine!") == "Numbers 123 are fine"


def test_remove_punctuation_emojis_preserved():
    """Test that emojis are preserved in the output."""
    assert remove_punctuation("Emojis 😀 stay too!") == "Emojis 😀 stay too"


def test_remove_punctuation_type_error_int():
    """Test that TypeError is raised for integer input."""
    with pytest.raises(TypeError):
        remove_punctuation(123)


def test_remove_punctuation_type_error_none():
    """Test that TypeError is raised for None input."""
    with pytest.raises(TypeError):
        remove_punctuation(None)


def test_remove_punctuation_only_punctuation():
    """Test that string with only punctuation returns empty string."""
    assert remove_punctuation("!!??...") == ""


def test_remove_punctuation_whitespace_preserved():
    """Test that whitespace characters (spaces, tabs, newlines) are preserved."""
    assert remove_punctuation("Hello,\tWorld!\nHow are you?") == "Hello\tWorld\nHow are you"


def test_remove_punctuation_unicode_preserved():
    """Test that unicode letters (accented characters) are preserved."""
    assert remove_punctuation("Café résumé!") == "Café résumé"


def test_remove_punctuation_type_error_list():
    """Test that TypeError is raised for list input."""
    with pytest.raises(TypeError):
        remove_punctuation(["hello", "world"])
