#!/usr/bin/env python3
""" Task 10 module """
from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Just trying to implement the Duck typing since it's determined by
    the behavour rather than an explicit type declaration
    """
    if lst:
        return lst[0]
    else:
        return None
