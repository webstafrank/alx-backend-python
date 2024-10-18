#!/usr/bin/env python3
"""
This module contains the wait_random coroutine which generates a random
delay between 0 and a specified max_delay.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    seconds and returns the delay.
    
    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.
        
    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)  # Generate a random float
    await asyncio.sleep(delay)  # Wait for the random delay
    return delay  # Return the delay

