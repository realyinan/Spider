import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'request'
}

response = requests.post(url, headers=headers, data=data)
res = response.json()
print(res)
print(res['data'][0]['v'])
