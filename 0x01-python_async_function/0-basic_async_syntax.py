#!/usr/bin/env python3
"""Task 0 module"""

import asyncio
import random

async def wait_random(max_delay=10):
    """ Waits for a random number of seconds """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
