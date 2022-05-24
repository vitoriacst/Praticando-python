import random
A1=str(input('primeiro aluno: '))
A2=str(input('segundo aluno: '))
A3=str(input('terceiro aluno: '))
A4=str(input('quarto aluno: '))
alunos = [A1,A2,A3,A4]
escolha = random.choice(alunos)
print('o escolhido foi : {}'.format(escolha))
