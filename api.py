import json
from igdb.wrapper import IGDBWrapper
from settings import ID, TOKEN

wrapper = IGDBWrapper(ID, TOKEN)

"""With a wrapper instance already created"""
# JSON API request
byte_array = wrapper.api_request(
    "games", 'fields name, platforms; search "destiny";')
# parse into JSON however you like...
result = json.loads(byte_array)

print(result)
