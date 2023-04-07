#!/usr/bin/python3
"""
this is the Unnitest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([5, 2, 4, 7, 1]), 7)
        self.assertEqual(max_integer([-2, -1, 5, 0]), 5)
        self.assertEqual(max_integer([-48, -9, -197, -8]), -8)
        self.assertEqual(max_integer([-1, -3, -5, 0]), 0)
        self.assertEqual(max_integer([9, 5, 7, 2]), 9)
        self.assertEqual(max_integer([9]), 9)

    def test_none_max_integer(self):
        self.assertIsNone(max_integer([]))
