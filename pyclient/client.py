import requests


auth_token = 'http://127.0.0.1:8000/token-auth/'
data = {
    'username': 'stuff',
    'password': 'suhdaud123'
}
response = requests.post(auth_token, data=data)




if response.status_code == 200:
    token = response.json()['token']


#get list of authors with token
endpoint = 'http://localhost:8000/api/authors/'
headers = {
    'Authorization': f'Token {token}'
}
response = requests.get(endpoint, headers=headers)
print(response.json())


