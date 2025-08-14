#!/usr/bin/env python
"""Complex types - functions"""
from typing import Callable
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument and returns a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
