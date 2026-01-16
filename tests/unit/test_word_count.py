import pytest
from textutils.textutils import word_count


def test_word_count_normal_sentence():
    assert word_count("Hello world") == 2


def test_word_count_extra_spaces():
    assert word_count("  This   is a test ") == 4


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_only_whitespace():
    assert word_count("     ") == 0


def test_word_count_with_punctuation():
    assert word_count("Hello, world!") == 2


def test_word_count_non_string_input():
    with pytest.raises(TypeError, match="Input text must be a string"):
        word_count(123)