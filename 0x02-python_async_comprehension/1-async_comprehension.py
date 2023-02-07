#!/usr/bin/env python3
"""Task 1 module"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A fuction that return 10 random numbers using an async comprehensing
    over async_generator
    """
    result = [i async for i in async_generator()]
    return result
