import json
import requests


endpoint = 'http://localhost:5000/hoteis/meuhotel2'

body_hotel_id = {
    'nome': 'Meu Hotel2',
    'estrelas': 4.8,
    'diaria': 398.90,
    'cidade': 'Santos',
    'site_id': 1
}

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDc5MTg2MSwianRpIjoiMzA4OWQ4ZTItOTAyMy00M2RjLWE0NjgtMmVlN2M1YjM2N2NjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0NzkxODYxLCJleHAiOjE2NjQ3OTI3NjF9.VeKgZFCC3YS9NLBCAUwh9SZgKEKoc5FkxBSO5-F1iJI'

hotel_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token 
}


response = requests.request('PUT', endpoint, json=body_hotel_id, headers=hotel_headers)
print(response.status_code)
print(response)

