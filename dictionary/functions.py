def question ():
  return input(
    "O que deseja realizar? \n" + "<I> - para inserir um usuario \n" + "<P> - Para pesquisar um usuario\n" + "<E> - Para excluir um usuario\n" + "<L> - Para listar um usuario"
    ).upper()

def inserir (dicionário):
    dicionário[input("Digite o Login: ").upper()]=[
    input("Digite o nome: ").upper(),
    input("Digite a última data de acesso: "),
    input("Qual a última estacão acessada: ")
    ]

