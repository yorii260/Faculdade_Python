"""
05) Neste exercício, deve ser feita validação dos dados de entrada juntamente o try/except. O
usuário deverá informar a quantidade de jogadores que deverá cadastrar no sistema. O sistema
deve salvar o nome do jogador, nº de partidas jogadas e a quantidade e gols feita em cada
partida. Os dados devem ser salvos em um dicionário juntamente com o total de gols feitos no
campeonato e em seguida criar uma lista com os jogadores cadastrados. O programa deverá
exibir os dados cadastrados com um menu de opções, onde o usuário deve informar um código
válido de um jogador cadastrado e o sistema deverá exibir os dados do jogador informado. O
usuário deve ser consultado quando deseja sair do programa.
"""

jogadores = []
jogador = {}


while True:
    
    try:
        
        qty_jogadores = int(input("Digite a quantidade de jogadores que deseja analisar: "))
    
        if qty_jogadores <= 0:
            raise ValueError
        
    except ValueError:
        print("A quantidade de jogadores deve ser maior do que zero.")
        continue 
    
    for i in range(1,qty_jogadores):
        nome = input(f"Digite o nome do(a) {i}° jogador(a): ").strip().title()
        
        if len(nome) < 0:
            print(f"O nome não deve ficar em branco, tente novamente.")
            continue 
        elif nome.isnumeric() or True in [f.isnumeric() for f in nome]:
            print("O nome deve ser composto de letras, e não números.")
            continue 
        
        try:
            qty_de_partidas = int(input(f"Digite a quantidade de partidas que o {i}° jogador fez: "))
            
            if qty_de_partidas < 0:
                raise ValueError
        
        except ValueError:
            print("Esperava-se números positivos, provavelmente digitastes letras ou números negativos.")
            continue
    

    break
    
     # Dps termino // sai
    
    