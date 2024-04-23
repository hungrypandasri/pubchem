# File: pubchem_toolkit/autocomplete.py

import requests

def autocomplete_search(query, dictionary, limit=10):
    """
    Perform auto-complete search using PubChem REST auto-complete API.

    Args:
        query (str): Search query.
        dictionary (str): Dictionary to search in (e.g., 'compound', 'gene', 'taxonomy', 'assay').
        limit (int): Maximum number of returned results (default is 10).

    Returns:
        list: List of suggested terms matching the query.
    """
    base_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/{dictionary}/{query}/json"
    params = {'limit': limit}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'dictionary_terms' in data:
            return data['dictionary_terms'][dictionary]
        else:
            return []
    else:
        raise Exception("Failed to perform auto-complete search. Check your query and try again.")
