import json
import requests
from bs4 import BeautifulSoup

page = requests.get('https://genius.com/Aesop-rock-gopher-guts-lyrics')
html = BeautifulSoup(page.text, "html.parser")

lyrics = html.find("div", class_="lyrics").get_text()
print(lyrics)
