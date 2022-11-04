import json
import requests


endpoint = 'http://localhost:5000/hoteis/meuhotel'

body_hotel_id = {
    'nome': 'Meu Hotel alterador',
    'estrelas': 4.8,
    'diaria': 398.90,
    'cidade': 'Santos',
    'site_id': 1
}

token = ' eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDc5MDg1OSwianRpIjoiYjk4ZWMzZWYtZjMxNC00MTVlLThjOGEtMmI3ZmFhMWIwYzJjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0NzkwODU5LCJleHAiOjE2NjQ3OTE3NTl9._CZGln0XWO5Dle7CktmvHRf2ix6kvZ-JO8zbhFWb54w'

hotel_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token 
}


response = requests.request('PUT', endpoint, json=body_hotel_id, headers=hotel_headers)
print(response.status_code)
print(response)

