#!/usr/bin/env python3
"""
Description:
A function to be validated in 
mypy and apply changes if
needed
"""

from typing import Any, Mapping, Tuple, Union, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Variable Annotation.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
