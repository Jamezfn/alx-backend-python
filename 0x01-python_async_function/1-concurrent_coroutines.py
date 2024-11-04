#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random delays and return them sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_times = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        wait_times.append(delay)

    return sorted(wait_times)
