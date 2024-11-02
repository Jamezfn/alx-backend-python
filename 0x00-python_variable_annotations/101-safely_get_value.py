#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retreives a value from dict using a given key
    """
    if key in dct:
        return dct[key]
    else:
        return default
