import csv

# lê os dados
with open("graduacao_unb.csv", encoding = "utf-8") as file:
    graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

    # a linha de cabeçalhos é utilizada como chave do dicionário
    # agrupa cursos por departamento
    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1

# abre um arquivo para escrita
with open("new_department_report.csv", "w", encoding = "utf-8") as file:
    # os valores a serem escritos devem ser dicionários
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    # É necessário passar o arquivo e o cabeçalho
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    # escreve as linhas de dados
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = {"Departamento": department, "Total de Cursos": grades}
        writer.writerow(row)
