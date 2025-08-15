#!/usr/bin/env python
"""Measure the runtime"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import asyncio
def measure_time(n, max_delay) -> float:
    """Measure the average execution time for wait_n."""
    starttime = time.time()
    asyncio.run(wait_n(n, max_delay))
    stoptime = time.time()
    total_time = stoptime - starttime
    return total_time / n
