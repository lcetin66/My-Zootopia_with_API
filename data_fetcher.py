"""
This module fetches the animals data for the animal 'animal_name'.
"""
import requests

API_KEY = 'S2laHELD7bSeHLjhhNBhcEv1Goyc1h3TCh2JbbrQ'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': API_KEY}
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
    except (Timeout, HTTPError, RequestException) as err:
        print(f"Error: {err}")
        return None
    
    return resp.json()