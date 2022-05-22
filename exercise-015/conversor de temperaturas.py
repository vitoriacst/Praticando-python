from cgi import print_form


TemEmCelsius = int(input('qual e a temperatura em celsius?'))
TempEmFahrenheit = (TemEmCelsius*9/5)+32

print('a temperatura em Fahrenheit e : {}'.format(TempEmFahrenheit))