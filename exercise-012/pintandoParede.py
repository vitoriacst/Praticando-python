largura = int(input('Qual e a largura da sua parede?'))
Altura = int(input('Qual e a altura da sua parede?'))
areaTotal = largura * Altura
print('Sua parede tem a deminsao de {}X{} e a sua area e de {}m'.format(largura,Altura,areaTotal))
tinta = areaTotal / 2
print('para pintar uma parede vc precisa de {}L'.format(tinta))