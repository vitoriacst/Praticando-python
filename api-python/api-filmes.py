import json

import requests

req = None

try:
 req = requests.get('https://solyd.com.br/')
except:
  print('erro')
  exit()

dicionario = json.loads(req.text)

#pega um texto que esta estruturado como um json e transforma em um dicionario

print(dicionario)
