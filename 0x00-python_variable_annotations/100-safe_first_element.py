#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
