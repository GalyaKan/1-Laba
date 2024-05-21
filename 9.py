import pytest
def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def test_empty_string():
    assert count_chars("") == {}

def test_single_character():
    assert count_chars("a") == {"a": 1}

def test_multiple_characters():
    assert count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}

def test_case_sensitive():
    assert count_chars("Hello World") == {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1}

def test_non_string():
    with pytest.raises(TypeError):
        count_chars(123)

def test_iterable_non_string():
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])