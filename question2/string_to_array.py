"""
A non-negative integer may be represented in a string with or without commas,
for example: "127,012,436" or "127012436".

A non-negative integer may be encoded as an array, where the value at each 
index represents 10 raised to the power of the index. For example, the value 
12436 would be encoded as the array [6, 3, 4, 2, 1] because:

6*10^0 + 3*10^1 + 4*10^2 + 2*10^3 + 1*10^4 = 12436

Write a Python function that encodes an integer represented as a string with or
without commas into an array like the one described above. You may choose to
use recursion OR iteration for this problem. You may add additional parameters
as needed provided that the parameters have default values.

Hint: can you make a copy of the string with the commas removed?

A pytest unit test has been provided to you to verify that your function is
working properly.
"""

import arrays


def string_to_array(a_string):
    """
    A Python function that encodes an integer represented as a string with or
    without commas into an array like the one described above.
    """
    a_string_trimmed = rem_commas(a_string)
    str_len = len(a_string_trimmed)
    ret_array = arrays.Array(str_len)
    for index in range(0, str_len):
        ret_array[index] = a_string_trimmed[str_len - (index + 1)]
    return ret_array


def rem_commas(a_string):
    """
    A Python function that takes in a string with commas and returns
    the same string with commas removed.
    """
    ret_string = ""
    for letter in a_string:
        if letter != ',':
            ret_string += letter
    return ret_string


def main():
    print(string_to_array("127,012,436"))


if __name__ == "__main__":
    main()
