import sys
import time

import requests

requisicao = requests.get('https://solyd.com.br/')

print(requisicao.status_code)
print(requisicao.text)
print(requisicao.headers)


