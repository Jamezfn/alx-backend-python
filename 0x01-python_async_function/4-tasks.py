#!/usr/bin/env python3
"""
Tasks
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
import asyncio

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        wait_times.append(delay)
        
    return sorted(wait_times)
