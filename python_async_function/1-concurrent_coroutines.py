#!/usr/bin/env python3
"""
Description:
An async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
"""

from typing import List
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Returns a of all delays (float values)
    in ascending order.
    """

    SpawnL = []
    DelayL = []

    for I in range(n):
        DelayedTask = asyncio.create_task(wait_random(max_delay))
        DelayedTask.add_done_callback(lambda X: DelayL.append(X.result()))
        SpawnL.append(DelayedTask)

    for SPAWN in SpawnL:
        await SPAWN

    return DelayL
