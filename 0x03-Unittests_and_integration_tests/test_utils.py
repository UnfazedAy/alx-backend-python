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
from unittest.mock import MagicMock, patch
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


# start of task 0
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

    # start of task 1
    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({"a": 1}, ('a', 'b'), KeyError)
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


# start of task 2
class TestGetJson(unittest.TestCase):
    """The TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
        mock_request: Callable
    ) -> None:
        """Test the get_json methods from utils.py"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_request.get_return_value = mock_response

        self.assertNotEqual(get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
