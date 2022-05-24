import math
co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjascente: '))
h1 = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(h1))

