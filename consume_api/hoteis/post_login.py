
import json
import requests


url = 'http://localhost:5000/login'

body_login = {
    "login": "admin",
    "senha": "abcd"
}

headers_login = {
    "Content-Type": "application/json"
}


response = requests.request(
        'POST', 
        url, 
        json=body_login, 
        headers=headers_login)

print(response.json())
print(response.status_code)

