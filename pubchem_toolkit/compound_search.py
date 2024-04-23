# File: pubchem_toolkit/compound_search.py

import requests


def get_compound_properties(compound_name):
    """
    Retrieve compound properties from PubChem API based on compound name.

    Args:
        compound_name (str): Name of the compound.

    Returns:
        dict: Dictionary containing compound properties.
    """
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{}/json"
    url = base_url.format(compound_name)

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        properties = data["PC_Compounds"][0]["props"]
        compound_properties = {}
        for prop in properties:
            label = prop["urn"]["label"]
            if "sval" in prop["value"]:
                value = prop["value"]["sval"]
            elif "ival" in prop["value"]:
                value = prop["value"]["ival"]
            elif "fval" in prop["value"]:
                value = prop["value"]["fval"]
            else:
                value = None
            compound_properties[label] = value
        return compound_properties
    else:
        raise Exception(
            "Failed to retrieve compound properties. Check compound name and try again."
        )
