users = {}
emails = ["example@email.com","name@email.com"]

tupla = list(enumerate(emails))

print(tupla)

for key in range(0,len(tupla)):
  print("Email", tupla[key][1])
  users[tupla[key]]=[input("Write the name: "), input("Write the level: ")]

for key, data in users.items():
  print("users: ", key[0])
  print("Email: ", key[1])
  print("name: ", data[0])
  print("level: ", data[1])


my_tupla = ('vivi' , 'Gabriel')
# a tupla não é mutável ,não podemos mudar o tamanho da tupla, utilizamos quando querendo algo fixo.


