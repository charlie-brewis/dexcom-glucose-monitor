import requests

url = "https://api.dexcom.com/v3/users/self/devices"

headers = {"Authorization": "Bearer tKZytUCDq5u8AtTb0lC09NYnyDU8mxIv"}

response = requests.get(url, headers=headers)

data = response.json()
print(data)