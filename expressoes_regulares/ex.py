import re

string_teste = 'o gato e bonito'

padrao = re.search(r'',string_teste) # r transforma em raw string
 #padrao e onde eu vou procurar

print(padrao.group())
