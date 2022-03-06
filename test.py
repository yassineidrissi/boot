import requests
import json
from bs4 import BeautifulSoup
 
url = "https://candidature.1337.ma/piscines"

r = requests.get(url)
print(r)
