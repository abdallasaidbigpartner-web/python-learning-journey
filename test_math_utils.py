"""
Lesson 14: Testing with pytest

Demonstrates writing automated unit tests that verify code behavior
- a core professional practice that proves correctness beyond a
single manual run, and catches regressions if code changes later.
"""

from math_utils import add, square

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_square():
    assert square(4) == 16
    assert square(0) == 0
    assert square(-3) == 9
