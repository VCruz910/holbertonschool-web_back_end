#!/usr/bin/env python3
"""
Description:
A type-annotated function
(floor) which takes a float (n)
as argument and returns the
floor of the float.
"""


def floor(n: float) -> int:
    """
    Returns the floor of
    the float.
    """
    return n if n >= 0 else (n) - 1
