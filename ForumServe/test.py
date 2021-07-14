import requests,pprint

payload = {
    'username' : 'root',
    'password' : '12345'
}

response = requests.post(' http://127.0.0.1:8000/login',data=payload)


pprint.pprint(response.json())