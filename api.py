import json
from igdb.wrapper import IGDBWrapper
from settings import ID, TOKEN

wrapper = IGDBWrapper(ID, TOKEN)

def query(endpoint: str, fields: str, where: str) -> list:
    """Query the API with desired parameters"""
    request = wrapper.api_request(
        f"{endpoint}, fields {fields}; where {where}"
    )
    result = json.loads(request)
    return result

def query_search(endpoint: str, search: str, fields: str = "name") -> list:
    """Search the API with desired parameters"""
    request = wrapper.api_request(
        endpoint, f'fields {fields}; search "{search}";'
    )
    result = json.loads(request)
    return result

def query_video(where: str) -> list:
    """Get a selection of Youtube links based on selected game"""
    request = wrapper.api_request(
        'game_videos', f'fields video_id; where game={where};'
    )
    result = json.loads(request)
    return result
