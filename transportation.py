from config import config
import json
import requests
from config import config


class transportation(object):
    def getResult(self, queryString):
        headers = {
            'User-Agent': '',
            'Authorization': 'Bearer ' + config.SECRETS["genius_access_token"]
        }

        response = requests.get(queryString, headers=headers)

        # Print lovely json to see wtf is actually going on
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=2))
        return parsed
