# -*- coding: utf-8 -*-
import json
import requests 

URL:str = 'http://localhost:5000'
endpoint_user_id:str = URL + '/usuarios/2'
token:str = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NTk5OTg2NCwianRpIjoiZTA2NjEzZDgtNTBlYy00Y2M1LTg0MTMtM2RiMzA0ZTRkY2ViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY1OTk5ODY0LCJleHAiOjE2NjYwMDA3NjR9.esK3o0QDpIQHXfYm-CthSJx9KekQFMFAM84wv8AiMkY' 


headers_user_id: dict[str, str] = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}


resposta_user_id = requests.request('DELETE',endpoint_user_id,headers=headers_user_id)


print(resposta_user_id.status_code)
print(resposta_user_id.json())



