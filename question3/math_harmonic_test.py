"""
Unit tests provded to verify that the implementation of the harmoics
function is working correctly for at least some test cases.

Additional test cases may be used when grading the function.
"""

from math_harmonic import *

""" Uncomment tests one at a time to test your solutions """


def test_harmonics_base():
    # setup
    expected = 1

    # invoke
    actual = harmonics(1)

    # analyze
    assert actual == expected


def test_harmonics_inv():
    # setup
    expected = None

    # invoke
    actual = harmonics(-1)

    # analyze
    assert actual == expected


def test_harmonics_general():
    # setup
    expected = 2.2833

    # invoke
    actual = harmonics(5)

    # analyze
    assert round(actual, 4) == expected


test_harmonics_general()
