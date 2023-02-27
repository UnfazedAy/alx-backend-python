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
from utils import access_nested_map, get_json, memoize


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

        self.assertTrue(get_json(test_url), test_payload)


# start of task 3
class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
