"""Tests for validation.py.

TODO: Implement this test once validate_isbn is implemented in
src/data_processing/validation.py.
"""

from data_processing.validation import validate_isbn

def test_valid_isbn():
    result = validate_isbn('9780306406157')
    assert result == '9780306406157'

def test_valid_isbn():
    result = validate_isbn('9780306406157')
    assert result == '9780306406157'

def test_invalid_isbn():
    result = validate_isbn('not-an-isbn')
    assert result is None

def test_wrong_length():
    result = validate_isbn('123456789')
    assert result is None

# from data_processing.validation import validate_isbn

# def test_valid_isbn():
#     result = validate_isbn('9780306406157')
#     assert result == '9780306406157'

# def test_invalid_isbn():
#     result = validate_isbn('not-an-isbn')
#     assert result is None

# def test_wrong_length():
#     result = validate_isbn('123456789')
#     assert result is None