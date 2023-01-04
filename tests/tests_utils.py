"""
Tests for the utils module.
author: @jocerfranquiz
date: 2022-12-02
version: 0.0.1
"""

import pytest
from src.kladia import dict_nested_order, get_size


# Path: tests\tests_utils.py
# Compare this snippet from examples\graph_examples.py:

# Test dict_nested_order function
def test_dict_nested_order():
    assert dict_nested_order({}) == 0
    assert dict_nested_order({'a': 1}) == 1
    assert dict_nested_order({'a': {'b': {'c': 1}}}) == 3
    assert dict_nested_order({'a': {'b': {'c': 1}}, 'd': 2}) == 3
    assert dict_nested_order({'a': {'b': {'c': 1}}, 'd': {'e': 2}}) == 3
    assert dict_nested_order({'a': {'b': {'c': 1}}, 'd': {'e': {'f': 2}}}) == 3
    assert dict_nested_order({'a': {'b': {'c': 1}}, 'd': {'e': {'f': {'g': 2}}}}) == 4


# Test get_size function
def test_get_size():
    assert get_size(1) == 28
    assert get_size('a') == 50
    assert get_size([1, 2, 3]) == 172
    assert get_size({'a': 1, 'b': 2, 'c': 3}) == 466
    assert get_size([]) == 56


# Run the tests script
if __name__ == '__main__':
    pytest.main()
