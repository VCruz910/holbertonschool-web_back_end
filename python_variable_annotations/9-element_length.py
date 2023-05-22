#!/usr/bin/env python3
"""
Description:
A function that returns values
with the appropiate types.
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns value with
    appropiate types.
    """
    return [(i, len(i)) for i in lst]
