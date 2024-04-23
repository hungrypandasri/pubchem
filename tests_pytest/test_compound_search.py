

# File: tests_pytest/test_compound_search.py

import pytest

from pubchem_toolkit.compound_search import get_compound_properties

def test_valid_compound_search():
    properties = get_compound_properties("aspirin")
    assert properties is not None
    assert isinstance(properties, dict)

def test_invalid_compound_search():
    with pytest.raises(Exception):
        get_compound_properties("nonexistentcompound")

