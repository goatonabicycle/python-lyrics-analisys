import json
import requests
from config import config

# this is Aesop Rock's genius artist id. This is pretty important at the moment.
artistId = 178
querystring = "https://api.genius.com/artists/" + \
    str(artistId) + "/songs?per_page=50"

headers = {
    'User-Agent': '',
    'Authorization': 'Bearer ' + config.SECRETS["genius_access_token"]
}

response = requests.get(querystring, headers=headers)

# Print lovely json to see wtf is actually going on
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=2))

# Here we start doing magic things
for item in parsed['response']['songs']:
    if item["primary_artist"]["id"] == artistId:
        print(
            " - songid:", item['id'],
            "\n - full_title:", item['full_title'],
            "\n - title_with_featured:", item['title_with_featured'],
            "\n - url:", item['url']
        )
        print("----")
