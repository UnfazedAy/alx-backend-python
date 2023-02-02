#!/usr/bin/env python3
""" Task 5 module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    performs a sum operation
    Args:
        input_list (list[float]): Takes in a list of floating numbers

    Returns:
        float: returns floats as the result
    """
    result = sum(input_list)
    return float(result)
