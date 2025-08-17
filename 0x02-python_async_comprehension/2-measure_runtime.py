#!/usr/bin/env python
"""Run time for four parallel comprehensions"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import time
async def measure_runtime():
    """Run async_comprehension 4 times in parallel and measure runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(10)))
    end = time.time()
    return end - start
