import json
from igdb.wrapper import IGDBWrapper
from settings import ID, TOKEN

wrapper = IGDBWrapper(ID, TOKEN)

def query(endpoint: str, fields: str = None, where: str = None) -> list:
    """Query the API with desired parameters"""
    request = wrapper.api_request(
        f"{endpoint}, fields {fields}; where {where}"
    )
    result = json.loads(request)
    return result

def query_search(endpoint: str, fields: str = "name", search: str = None) -> list:
    """Search the API with desired parameters"""
    request = wrapper.api_request(
        endpoint, f'fields {fields}; search "{search}";'
    )
    result = json.loads(request)
    return result
