"""Defines a simple date matcher."""

import pynini

import year

_month = pynini.union(
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
# This is just one way to do it...
_day = pynini.union(*(str(i) for i in range(32)))

DATE = _month + " " + _day + ", " + year.YEAR
