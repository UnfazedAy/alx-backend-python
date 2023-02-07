#!/usr/bin/env python3
"""Task 2 module"""

import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Using async comprehension and time function
    to measure runtime of 4 parallel async comprehensions.
    """
    start_time = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end_time = time.perf_counter()
    return (end_time - start_time)
