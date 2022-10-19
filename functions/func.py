

def calculator(num1,num2):
   if(num1>num2):
     return num1
   if(num2>num1):
     return num2
   return 'f'

  #🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

def media(num1 , num2):
   value = num1 + num2 / 2
   return value

def mean(numbers):
     total = 0
     for number in numbers:
         total += number
     return total / len(numbers)

names_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def names(names_list:str):
  biggest = names_list[0]
  for name in names_list:
    if len(name) > len(biggest):
      biggest = name
  return biggest
