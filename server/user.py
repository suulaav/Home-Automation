import requests

token = None
response = requests.post('http://localhost:5000/auths', json={"userName": "Sulav", "password": "password"})

if response.json():
    token = response.json()['data']["token"]

response = requests.post('http://localhost:5000/bedroom', headers={'token': token}, json={"Light 1": "1",
                                                                                          "Light 2": "2"})

print(response.json())
