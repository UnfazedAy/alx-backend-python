#!/usr/bin/env python3
""" Task 9 module """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that computes the length of each iterables in lst
    """
    return [(i, len(i)) for i in lst]
