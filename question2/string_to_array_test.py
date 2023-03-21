"""
A unit test provded to verify that the implementation of the string_to_array
function is working correctly for at least some test cases.

Additional test cases will be used when grading the function.
"""

from string_to_array import *

""" Uncomment tests one at a time to test your solutions """

def test_string_to_array_empty():
    # setup
    a_string = ""
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 0 == len (an_array)

def test_string_to_array_6():
    # setup
    a_string = "6"
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 1 == len(an_array)
    assert 6 == an_array[0]

def test_string_to_array_12346():
    # setup
    a_string = "12346"
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 5 == len(an_array)
    assert 6 == an_array[0]
    assert 4 == an_array[1]
    assert 3 == an_array[2]
    assert 2 == an_array[3]
    assert 1 == an_array[4]

def test_string_to_array_12346_comma():
    # setup
    a_string = "12,346"
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 5 == len(an_array)
    assert 6 == an_array[0]
    assert 4 == an_array[1]
    assert 3 == an_array[2]
    assert 2 == an_array[3]
    assert 1 == an_array[4]
    

# additional grading tests - do not provide to student
def test_string_to_array_000():
    # setup
    a_string = "000"
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 3 == len(an_array)
    assert 0 == an_array[0]
    assert 0 == an_array[1]
    assert 0 == an_array[2]

def test_string_to_array_9087654321_commas():
    # setup
    a_string = "9,087,654,321"
    
    # invoke
    an_array = string_to_array(a_string)

    # analyze
    assert 10 == len(an_array)
    assert 1 == an_array[0]
    assert 2 == an_array[1]
    assert 3 == an_array[2]
    assert 4 == an_array[3]
    assert 5 == an_array[4]
    assert 6 == an_array[5]
    assert 7 == an_array[6]
    assert 8 == an_array[7]
    assert 0 == an_array[8]
    assert 9 == an_array[9]
