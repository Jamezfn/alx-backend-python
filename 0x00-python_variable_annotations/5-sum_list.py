#!/usr/bin/env python
"""Complex types - list of floats"""

from typing import List
def sum_list(input_list: List[float]) -> float:
    """Takes a list input_list of floats as argument and returns their sum as a float."""
    return float(sum(input_list))
