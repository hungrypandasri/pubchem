# import pytest
# from pubchem_toolkit.auto_complete import autocomplete_search  # type: ignore


# def test_valid_autocomplete():
#     # Test auto-complete search for compounds
#     compounds = autocomplete_search("aspirin", dictionary="compound", limit=6)
#     assert compounds is not None
#     assert isinstance(compounds, list)
#     assert len(compounds) > 0

#     # Test auto-complete search for genes
#     genes = autocomplete_search("egfr", dictionary="gene", limit=5)
#     assert genes is not None
#     assert isinstance(genes, list)
#     assert len(genes) > 0

#     # Add more tests for other dictionaries (e.g., assays, taxonomy) if needed


# def test_invalid_autocomplete():
#     # Test auto-complete search with invalid query
#     invalid_result = autocomplete_search(
#         "nonexistentquery", dictionary="compound", limit=10
#     )
#     assert invalid_result == []



# File: tests_pytest/test_autocomplete_search.py

import pytest

from pubchem_toolkit.auto_complete import autocomplete_search

def test_valid_autocomplete_search():
    compounds = autocomplete_search("aspirin", dictionary="compound", limit=6)
    assert compounds is not None
    assert isinstance(compounds, list)
    assert len(compounds) > 0

def test_invalid_autocomplete_search():
    invalid_result = autocomplete_search("nonexistentquery", dictionary="compound", limit=10)
    assert invalid_result == []

