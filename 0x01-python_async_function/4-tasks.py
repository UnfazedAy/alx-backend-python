#!/usr/bin/env python3
"""Task 4 module"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that returns an asyncio.Task"""
    tasks = (task_wait_random(max_delay) for i in range(n))
    result = await asyncio.gather(*tasks)
    return (sorted(result))
