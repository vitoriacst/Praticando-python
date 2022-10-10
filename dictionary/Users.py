from functions import inserir, question

users = {}
options = question()

while options == "I" or options == "P" or options == "L":
  if options== "I":
    inserir(users)
  options = question()
