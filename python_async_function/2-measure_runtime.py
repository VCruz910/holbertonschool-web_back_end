#!/usr/bin/env python3
"""
Description:
A function with n integers and
max_delay as arguments that
measures the total execution
time for wait_n(n, max_delay),
and returns total_time / n.
"""

from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    for wait_n and returns total time / n.
    """

    Time_0 = time()
    run(wait_n(n, max_delay))
    Time_1 = time()
    ElapsedTime = Time_1 - Time_0
    return ElapsedTime / n
