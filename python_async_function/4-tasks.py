#!/usr/bin/env python3
"""
Description:
An async routine that takes 2
arguments and returns a list
of all delays.
"""

from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Returns a of all delays (float values)
    in ascending order.
    """

    SpawnL = []
    DelayL = []

    for I in range(n):
        DelayedTask = task_wait_random(max_delay)
        DelayedTask.add_done_callback(lambda X: DelayL.append(X.result()))
        SpawnL.append(DelayedTask)

    for SPAWN in SpawnL:
        await SPAWN

    return DelayL
