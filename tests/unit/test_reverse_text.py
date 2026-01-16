"""
Unit tests for the reverse_text function.

Tests cover basic functionality, edge cases, and error handling.
"""

import pytest
from textutils.textutils import reverse_text

def test_multiple_words_word_mode_returns_reversed():
    assert reverse_text('Hello World') == 'World Hello'

def test_multiple_words_char_mode_returns_reversed():
    assert reverse_text('Hello World', mode = 'char') == 'dlroW olleH'

def test_empty_string_word_mode_returns_empty():
    assert reverse_text('') == ''

def test_single_word_word_mode_returns_same_word():
    assert reverse_text('Hello') == 'Hello'

def test_leading_trailing_spaces_word_mode():
    assert reverse_text('  Hello World  ') == 'World Hello'