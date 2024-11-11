"""
04) Neste exercício, deve ser feita validação dos dados de entrada juntamente o try/except. O
programa deve ler os dados de uma pessoa: nome, sexo e idade salvando-os em um dicionário.
Deverá ser inserido em uma lista de pessoas. O usuário deverá informar se deseja continuar ou
não. Ao escolher a opção que não deseja continuar o programa deverá exibir:
a) A quantidade de pessoas cadastradas
b) A média de idade das pessoas cadastradas
c) Uma lista com o nome de todas as mulheres
d) Um lista com todas as pessoas (nome, sexo, idade) que estão com idade acima da média .
"""

from os import system 
peoples = []
people = {}

while True:
    
    nome = input("Digite o nome do usuário: ").strip().title()
    
    if len(nome) < 0:
        print(f"O nome não deve ficar em branco, tente novamente.")
        continue 
    elif nome.isnumeric() or True in [f.isnumeric() for f in nome]:
        print("O nome deve ser composto de letras, e não números.")
        continue 
    
    system("cls")
    sexo = input("Digite o sexo do usuário [F] para Feminino e [M] para Masculino.\n: ").strip().lower()
    
    if sexo in 'fm':
        
        try:
            idade = int(input("Digite a idade do usuário: "))
            
            if idade <= 0:
                print("A idade deve ser maior do que zero.")
                continue 
            
            people.update({"nome": nome, "idade": idade, "sexo": sexo})
            peoples.append(people.copy())
            
            again = input("Deseja continuar? [S] para Sim e [N] para Não.\n: ").lower()
            
            if again in 'sn':
                
                if again == 'n':
                    break 
                else:
                    people.clear()
                    continue 
            else:
                print("Opção inválida, por padrão, vamos continuar o programa para você.")
                continue 
            
        except ValueError:
            print("A idade é composta apenas por números, tente novamente.")
            continue
    else:
        print("Inserção incorreta, digite [F] para feminino e [M] para masculino, repita o processo desde o início.")
        continue

system("cls")

media_idade = 0 

for x in peoples:
    media_idade += x.get('idade')

    
print(f"Foram cadastradas {len(peoples)} pessoa{'s' if len(peoples) > 1 else ''}.")
print(f"A média de idade é de {round(media_idade/len(peoples),1)} anos.")

moileres = []
for y in peoples:
    if y.get("sexo") == 'f': moileres.append(y.get("nome"))

print(f"As mulheres registradas são: {', '.join(moileres)} | {moileres}")
    

print("Relação de pessoas acima da média de idade.")
for z in peoples:
    if int(z.get("idade")) > media_idade/len(peoples):
        print(f"Nome: {z.get('nome')} | sexo: {z.get('sexo')} | idade: {z.get('idade')} ano{'s' if int(z.get('idade')) > 1 else ''}.")
    
    
    
    
        
    
    