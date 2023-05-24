#!/usr/bin/env python3
"""
Description:
A function that gets the
key in a dictionary.
"""

from typing import TypeVar, Union, Mapping, Any

TV = TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TV, None] = None) -> Union[Any, TV]:
    if key in dct:
        return dct[key]
    else:
        return default
