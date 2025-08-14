#!/usr/bin/env python
"""Complex types - string and int/float to tuple"""

from typing import Union, Tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple (k, v squared). Annotated so the second element is a float."""
    return (k, v ** 2)
