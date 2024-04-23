# File: tests/test_compound_search.py

import unittest
from pubchem_toolkit.compound_search import get_compound_properties


class TestCompoundSearch(unittest.TestCase):
    def test_valid_compound(self):
        properties = get_compound_properties("aspirin")
        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, dict)

    def test_invalid_compound(self):
        with self.assertRaises(Exception):
            get_compound_properties("nonexistentcompound")


if __name__ == "__main__":
    unittest.main()
