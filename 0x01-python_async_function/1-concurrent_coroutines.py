#!/usr/bin/env python3
"""
This module contains the wait_n coroutine which spawns wait_random
multiple times and returns a sorted list of random delays.
"""

import asyncio
from basic_async_syntax import wait_random  # Adjust the import as necessary

async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns wait_random n times with the specified max_delay and
    returns a sorted list of the delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        list: A list of random delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert delay in ascending order
        index = 0
        while index < len(delays) and delays[index] < delay:
            index += 1
        delays.insert(index, delay)

    return delays

