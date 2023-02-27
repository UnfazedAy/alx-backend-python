#!/usr/bin/env python3
"""This file contains the TestAccessNestedMap class"""
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """The TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ('a', ), 1),
        ({"a": {"b": 2}}, ('a', ), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        result: Any
    ) -> Any:
        """
        A method that tests the accesss_nested_map by checking if the
        nested_map is equal to the path and expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({"a": 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        result: Any
    ) -> Any:
        """
        A method that tests the accesss_nested_map by checking if there's
        an Exception Error and hence uses the assertRaises method
        to throw an errow message
        """

        with self.assertRaises(result):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
