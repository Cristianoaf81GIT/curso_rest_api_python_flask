# -*- coding: utf8 -*-

import json
import requests 


endpoint_cadastro = 'http://localhost:5000/cadastro'
body_cadastro = {
    'login': 'josef',
    'senha': 'abcde'
}


headers_cadastro = {
    'Content-Type': 'application/json'
}

resposta_cadastro = requests.request('POST', 
                                     endpoint_cadastro, 
                                     json=body_cadastro, headers=headers_cadastro)


print(resposta_cadastro.status_code) 
print(resposta_cadastro.json())



