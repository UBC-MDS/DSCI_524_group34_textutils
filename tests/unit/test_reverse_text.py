"""
Unit tests for the reverse_text function.

Tests cover basic functionality, edge cases, and error handling.
"""

import pytest
from textutils.textutils import reverse_text

def test_multiple_words_word_mode_returns_reversed():
    """Tests that multiple words are reversed in the default word mode."""
    assert reverse_text('Hello World') == 'World Hello'

def test_multiple_words_char_mode_returns_reversed():
    """Tests that all characters are reversed when using character mode."""
    assert reverse_text('Hello World', mode = 'char') == 'dlroW olleH'

def test_empty_string_word_mode_returns_empty():
    """Tests that an empty string returns an empty result in word mode."""
    assert reverse_text('') == ''

def test_single_word_word_mode_returns_same_word():
    """Tests that a single word is unchanged when using word mode."""
    assert reverse_text('Hello') == 'Hello'

def test_leading_trailing_spaces_word_mode():
    """Tests that leading and trailing spaces are ignored in word mode."""
    assert reverse_text('  Hello World  ') == 'World Hello'

def test_invalid_mode_raises_value_error():
    """Tests that an invalid mode raises a ValueError."""
    with pytest.raises(ValueError):
        reverse_text('Hello', mode = 'chicken tenders')

def test_non_string_input_raises_type_error():
    """Tests that a non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        reverse_text(12345)