import requests

token = str()
response = None


def login():
    return requests.post('http://localhost:5000/auths', json={"userName": "Sulav", "password": "password"}).json()


def get_data():
    global token
    global response
    response = login()
    try:
        token = response['data']['token']
    except Exception:
        pass
    while True:
        response = dict()
        response = requests.get('http://localhost:5000/bedroom', headers={'token': token}).json()
        if response.keys().__contains__('message') and response['message'] == 'Token is invalid!':
            token = login()['data']['token']
        if response.keys().__contains__('data'):
            print(response['data'])


get_data()
