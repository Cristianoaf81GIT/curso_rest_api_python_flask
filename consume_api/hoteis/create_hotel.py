import json
import requests


endpoint = 'http://localhost:5000/hoteis/meuhotel'

body_hotel_id = {
    'nome': 'Meu Hotel',
    'estrelas': 4.8,
    'diaria': 398.90,
    'cidade': 'Santos',
    'site_id': 1
}

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDI3NDA1NSwianRpIjoiZGNiZTNiNWEtMWQ4MS00NGYwLWJmYTctNDZkOTQ2MzdmMzdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY0Mjc0MDU1LCJleHAiOjE2NjQyNzQ5NTV9.F5ZIcaf6YioIKoyXS_ugnS7gUIZWeMKQCXHhGVg2MLw'

hotel_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token 
}


response = requests.request('POST', endpoint, json=body_hotel_id, headers=hotel_headers)
print(response.status_code)
print(response)

