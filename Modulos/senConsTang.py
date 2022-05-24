import math
an = float(input('digite o angulo que vc deseja encontrar: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('o angulo de {} tem o Seno de {:.2f} e o cosseno de {:.2f}'.format(an,seno,cosseno))
print('o angulo de {} tem a tangente de {:.2f}'.format(an,tangente))