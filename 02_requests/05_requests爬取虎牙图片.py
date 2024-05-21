import requests
from urllib import request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://www.douyu.com/wgapi/ordnc/live/web/room/yzList/1'

response = requests.get(url=url, headers=headers)
res = response.json()
with open(f'02_requests\huya.json', 'w') as json_file:
    json.dump(res, json_file, indent=4)

for zb in res['data']['rl']:
    name = zb['nn']
    img = zb['rs1']
    request.urlretrieve(url=img, filename=f"02_requests\images\{name}.jpg")
    request.urlcleanup()
