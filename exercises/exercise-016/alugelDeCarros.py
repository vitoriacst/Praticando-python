Days = int(input('quantidade dias de alugel?'))
Km = float(input('quantidade de km rodados?'))


valueDays = Days*60
valueKm = Km*0.15

Total = valueDays + valueKm

print('o valor a pagar foi de R${:.2f}'.format(Total))