"""Defines a year matcher."""

import pynini

from pynini.lib import byte

YEAR = byte.DIGIT**4

# Alternatively, if you don't want to use the predefined `DIGIT` automaton:
# YEAR = pynini.union("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") ** 4
