from config import config
import json
import requests
from bs4 import BeautifulSoup


class transportation(object):
    def getJsonResult(self, queryString, params):
        headers = {
            'User-Agent': '',
            'Authorization': 'Bearer ' + config.SECRETS["genius_access_token"]
        }

        response = requests.get(queryString, headers=headers, params=params)

        # Print lovely json to see wtf is actually going on
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=2))
        return parsed

    def getPageResult(self, queryString):
        page = requests.get('https://genius.com/Aesop-rock-gopher-guts-lyrics')
        html = BeautifulSoup(page.text, "html.parser")
        return html
