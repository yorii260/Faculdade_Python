"""
05) Faça um programa que ajude um jogador da megasena a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta
"""

from random import randint 

jogos = []
jogo = []

x = 0

while True:
    
    try:
        
        qty_jogos = int(input("[i] : Digite a quantidade de jogos a serem gerados: "))
        
        if qty_jogos > 0:
            
            while x < qty_jogos:
                
                jogo.append(f"[Jogo {x+1}] : Palpites")
                for i in range(0,6):
                    jogo.append(randint(1,60))
                    
                jogos.append(jogo[:])
                jogo.clear()
                x += 1 
            break
                        
        else:
            print(f"[!] : A quantidade de jogos deve ser maior ou igual a um.")
            continue
    
    except ValueError:
        print("Digite apenas números, tente novamente.")
        continue 


for z in jogos:
    
    numeros = [str(f) for f in z[1:]]
    
    print(f"{z[0]}\n-----------------\n{','.join(numeros)}\n")
