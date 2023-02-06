#!/usr/bin/env python3
"""Task 1 module"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executing multiple caroutines at the same time with async"""
    tasks = (wait_random(max_delay) for i in range(n))
    result = await asyncio.gather(*tasks)
    return (sorted(result))
