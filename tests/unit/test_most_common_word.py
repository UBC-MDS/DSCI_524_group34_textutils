"""
Unit tests for most_common_word() function. 
Tests cover case sensitivity, empty inputs, punctuation inputs,
tie-breaking behavior, and invalid input types.
"""

import pytest
from textutils.textutils import most_common_word


def test_most_common_word_wocap():
    """Test get the most common word based on case-insensitive"""
    expected = most_common_word("Hello. Hello. hello. How's your day?")
    assert expected == "hello"


def test_most_common_word_wcap():
    """Test get the most common word based on case-sensitive"""
    expected = most_common_word("Hello. Hello. hello. How's your day?", True)
    assert expected == "Hello"


def test_most_common_word_empty():
    """Test the empty input will return empty"""
    expected = most_common_word("")
    assert expected == ""


def test_most_common_word_space(): 
    """Test only space will return empty (space is ignored)"""
    expected = most_common_word("    ")
    assert expected == ""


def test_most_common_word_punctuation(): 
    """Test only punctuation will return empty (punctuation is ignored)"""
    expected = most_common_word("!!!!!!!!!!!!")
    assert expected == ""


def test_most_common_word_typeerror():
    """Test if incorrect input type (not str)"""
    with pytest.raises(TypeError):
        most_common_word(123)


def test_most_common_word_none():
    """Test if input is None"""
    with pytest.raises(TypeError):
        most_common_word(None)


def test_most_common_word_tie():
    """Test for tie situation, should return the first appearance word"""
    expected = most_common_word("apple banana apple banana")
    assert expected == "apple"


def test_most_common_word_single_word():
    """Test for single word"""
    expected = most_common_word("hello")
    assert expected == "hello"


def test_most_common_word_mixed_num():
    """Test for mixed text with numbers"""
    expected = most_common_word("hello, 123 - 123 345 !!123")
    assert expected == "123"