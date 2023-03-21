"""
math_harmonic.py
"""

"""
The harmonic series is a divergent infinite series that is defined as: 
1 + 1/2 + 1/3 + 1/4 + ... + 1/n
as n -> infinity

Write a recursive function, harmonics(t) that will compute and return part of the series, limited by a parameter t
I.e:  1 + 1/2 + 1/3 + .... + 1/t

The function should return None for any value of t less than 1.

"""


def harmonics(t):
    """
    Computes harmonic series until 1/t, recursively
    """
    if t == 1:
        return 1
    elif t < 1:
        return None
    else:
        return 1 / t + harmonics(t - 1)
