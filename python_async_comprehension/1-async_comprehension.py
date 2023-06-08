#!/usr/bin/env python3
"""
Imports the "async_generator" function from
the previous task and writes a coroutine
called "async_comprehension" that takes
no arguments.
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Return list of values yielded
    by async_generator.
    '''
    return [value async for value in async_generator()]
