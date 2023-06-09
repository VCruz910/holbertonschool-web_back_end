#!/usr/bin/env python3
"""
Description:
A function that gets the
key in a dictionary.
"""

from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Gets the key value in
    a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
