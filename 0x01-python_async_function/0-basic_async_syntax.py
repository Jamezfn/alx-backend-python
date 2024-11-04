#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a delay between 0 and max_delay seconds.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
