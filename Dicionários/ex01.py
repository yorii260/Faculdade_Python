"""
01) Faça um programa que leia o nome e a média de um aluno, salve os dados em um dicionário
juntamente com o status do aluno, se média maior ou igual a 6 ele é aprovado, caso contrário,
é reprovado. Exiba o boletim do aluno exibindo o nome, média e situação.
"""

alunos = []
aluno = {}


while True:
    
    try:
        nome = input("[abc] : Digite o nome do aluno(a): ").strip().title()
        media = float(input(f"[123] : Digite a média do aluno(a) {nome}: "))
        status = 'Aprovado' if media >= 6 else 'Reprovado'
        
        aluno.update({"nome": nome, "media": media, "status": status})
        alunos.append(aluno.copy())
        aluno.clear()
        break 
    except ValueError:
        print(f"Erro na digitação, revise e tente novamente.")
        continue

for i in range(0, len(alunos)):
    print(f"\n-> Nome do aluno(a): {alunos[i].get('nome')}\n-> Média Final: {alunos[i].get('media')}\n-> Situação: {alunos[i].get('status')}")
