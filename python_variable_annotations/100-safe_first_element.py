#!/usr/bin/env python3
"""
Description:
A function that checks
the first element safely.
"""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Checks elements safely.
    """
    if lst:
        return lst[0]
    else:
        return None
