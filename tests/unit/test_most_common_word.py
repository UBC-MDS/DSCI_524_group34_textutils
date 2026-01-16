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
    excepted = most_common_word("    ")
    assert excepted == ""


def test_most_common_word_punctuation(): 
    """Test only punctuation will return empty (punctuation is ignored)"""
    expected = most_common_word("!!!!!!!!!!!!")
    assert expected == ""


def test_most_common_word_typeerror():
    with pytest.raises(TypeError):
        most_common_word(123)


def test_most_common_word_none():
    with pytest.raises(TypeError):
        most_common_word(None)

