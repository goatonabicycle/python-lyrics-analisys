import json
import requests
from config import config

artistImLookingFor = 'aesop rock'  # todo: this should be more dynamic eventually
URL_SEARCH = "https://api.genius.com/search?q="
querystring = URL_SEARCH + artistImLookingFor

headers = {
    'User-Agent': '',
    'Authorization': 'Bearer ' + config.SECRETS["genius_access_token"]
}

response = requests.get(querystring, headers=headers)

# Print lovely json to see wtf is actually going on
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=2))
