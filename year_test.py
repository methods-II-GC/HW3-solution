"""Unit tests for year matcher."""

import unittest

from pynini.lib import rewrite

import year


class YearTest(unittest.TestCase):
    def matches(self, string: str):
        try:
            return rewrite.matches(string, string, year.YEAR)
        except rewrite.Error:
            return False

    def test_non_numeric(self):
        self.assertFalse(self.matches("foobar"))

    def test_4_digits(self):
        for number in [1555, 1648, 1815, 1919, 1973]:
            self.assertTrue(self.matches(str(number)))

    def test_wrong_numbers_of_digits(self):
        for number in [555, 55555]:
            self.assertFalse(self.matches(str(number)))


if __name__ == "__main__":
    unittest.main()
