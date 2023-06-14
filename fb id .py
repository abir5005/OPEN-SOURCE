#!/usr/bin/python

import requests
import re

url = 'https://www.facebook.com/zuck'
idre = re.compile('"entity_id":"([0-9]+)"')
page = requests.get(url)
print idre.findall(page.content)

# One-liner
# python -c 'import requests, re; print re.findall("\"entity_id\":\"([0-9]+)\"",