"""Unit tests for date matcher."""

import unittest

from pynini.lib import rewrite

import date


class DateTest(unittest.TestCase):
    def matches(self, string: str):
        try:
            return rewrite.matches(string, string, date.DATE)
        except rewrite.Error:
            return False

    def test_non_date(self):
        self.assertFalse(self.matches("Merch 14th, 999"))

    def test_january_24_1941(self):
        self.assertTrue(self.matches("January 24, 1941"))

    def test_april_4_1985(self):
        self.assertTrue(self.matches("April 4, 1985"))


if __name__ == "__main__":
    unittest.main()
