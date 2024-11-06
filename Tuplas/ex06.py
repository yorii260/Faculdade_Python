"""
06) Crie um programa que leia o nome, duas notas e a média das notas de “n” alunos e guarde
tudo em uma lista composta. No final, mostre o boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from os import system 


alunos = []
aluno = []

while True:
    
    try:
        
        nome = input("[abc] : Digite o nome do aluno(a): ").strip().title()
        notas = [int(f) for f in input(f"[123] : Digite as duas notas do aluno {nome}, separando-as por uma vírgula. : ").split(',')]
        
        aluno.append(nome)
        aluno.append(notas)
        aluno.append(sum(notas)/len(notas))
        
        alunos.append(aluno[:])
        aluno.clear()
        
        if input("[0] : Você deseja cadastrar outro aluno(a) ?\n: ").strip().lower() == 's':
            continue 
        else:
            break
        
    except ValueError:
        print("Ocorreu um erro em sua digitação, tente novamente.")
        continue
    
system('cls')
while True:
    
    print(
f"""
Faça sua escolha:

[0] -> Verificar todas as notas de todos os alunos(as) registrados. 
[1] -> Verificar a nota de um aluno(a) específico. 
[2] -> Sair do programa. 
"""
)
    try:
        esc = int(input("[123] : Faça sua escolha: "))
        
        match esc: 
            
            case 0:
                
                for i in range(0,len(alunos)):
                    
                    notas = ','.join(str(f) for f in alunos[i][1])
                    media = alunos[i][2]
                    nome = alunos[i][0]
                    
                    system('cls')
                    print(f"{nome} - Média final: {media}\nNotas: {notas}\n")
                break
            
            case 1:
                nomes = []
                
                for i in alunos: nomes.append(str(i[0]))
                
                print(f"Os alunos registrados são esses:\n{','.join(nomes)}")
                esc = input("Digite o nome do aluno(a) que deseja verificar individualmente: ").strip().title()
                
                if esc not in nomes:
                    print(f"O nome {esc} não está registrado, verifique novamente e repita o processo.")
                    break 
                else:
                    
                    notas = [str(f) for f in alunos[nome.index(esc)][1]]
                    media = alunos[nome.index(esc)][2]
                    
                    system('cls')
                    print(f"Informações do aluno(a) {nome}\n-> Média final: {media}\n-> Notas: {','.join(notas)}")
                    break 
            case 2: 
                break; 
        
        break 
    
    except ValueError:
        print("Digite apenas números, tente novamente.")
        continue
                
                