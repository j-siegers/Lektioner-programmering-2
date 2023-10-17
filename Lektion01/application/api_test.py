import json

import requests
choice = input('Choose an extra option: ')
url = f'http://127.0.0.1:5000/get-user/Johan?extra={choice}'
response = requests.get(url)
ret_dict = json.loads(response.text)

for key in ret_dict:
    print(key, ':', ret_dict[key])

