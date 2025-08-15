#!/usr/bin/env python
"""Execute multiple coroutines"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
async def wait_n(n: int, max_delay: int):
    """Spawn wait_random n times with max_delay, return delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)
    return delay
