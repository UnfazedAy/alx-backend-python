#!/usr/bin/env python3
"""Module for task 0"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Union, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """
    A class that uses unittest and parmetrization to verify
    utils.access_nested_map
    """

    # start of task 0
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_result: Union[Dict, int]
    ) -> None:
        """
        A method that tests the accesss_nested_map by checking if the
        nested_map is equal to the path and expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    # start of task 1
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_error(
        self,
        nested_map: Mapping,
        path: Sequence,
    ) -> None:
        """
        A method that tests the accesss_nested_map by checking if there's
        an Exception Error and hence uses the assertRaises method
        to throw an errow message
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


# class TestGetJson(unittest.TestCase):
#     """
#     A class that uses unittest and parmetrization to verify
#     utils.get_json functionality
#     """
#     @parameterized.expand([
#         ("http://example.com", {"payload": True}),
#         ("http://holberton.io", {"payload": False})
#     ])
#     def test_get_json(
#         self,
#         test_url: str,
#         test_payload: Dict
#     ) -> None:


if __name__ == "__main__":
    unittest.main(verbosity=2)
