import json
import requests

URL = 'http://localhost:5000'


#get /hoteis
resposta_hoteis = requests.request('GET', URL + '/hoteis')
hoteis = resposta_hoteis.json()
lista_hoteis = hoteis['hoteis']

print(resposta_hoteis.status_code)
print(resposta_hoteis.json())
print(hoteis['hoteis'][0])
print('total de hoteis: ' + str(len(hoteis['hoteis'])))
print('\n')

for hotel in lista_hoteis:
    print(hotel)

