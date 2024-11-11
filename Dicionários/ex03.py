"""
03) Faça um programa que analise o desempenho de um jogador de futebol solicitando o nome
do jogador, a quantidade de partidas que ele jogou e para cada partida deve informar a
quantidade de gols. Ao final, salve os dados digitados pelo usuário em um dicionário incluindo
o total de jogos que ele fez no campeonato. Exiba o dicionário, formatado, com o nome do
jogador e a quantidade de partidas que jogou durante o campeonato. Deve ser exibido a
quantidade de gols que o jogador fez por partida.
"""
from os import system

jogador = {}


while True:
    
    player_name = input("Primeiramente, digite o nome do jogador(a): ").strip().title()
    
    if len(player_name) > 0:
        
        qty_partidas = int(input(f"Digite a quantidade de partidas que o jogador {player_name} jogou em sua carreira: "))
    
    else:
        print(f"O nome do jogador(a) não deve ficar vazio, tente novamente.")
        continue 
    
    try:
        if qty_partidas > 0:
            
            system("cls")
            jogador.update({"nome": player_name, "qty_partidas": qty_partidas, "jogos": {}})
            
            i = 1
            gols_totais = 0
            while i <= qty_partidas:
                gols = int(input(f"Digite a quantidade de gols da {i}° partida: "))
                
                if gols < 0:
                    print("A quantidade de gols deve ser maior ou igual a zero!")
                    continue 
                
                gols_totais += gols 
                jogador.get("jogos").update({f"{i}_game": f"{gols} gol{'s' if gols > 1 else ''}"})
                i += 1
            
            jogador.update({"gols_totais": gols_totais})
            
            print(
                f"O jogador {jogador.get('nome')} esteve em {jogador.get('qty_partidas')} partida{'s' if qty_partidas > 1 else ''}")
            
            for key, item in jogador.get("jogos").items():
                print(f"Em sua {key.replace('_game','')}° partida, ele(a) marcou {item}.")
            
            print(f"Em toda sua carreira, o jogador {jogador.get('nome')} marcou um total de {jogador.get('gols_totais')} gol{'s' if jogador.get('gols_totais') > 1 else ''}! ({round(int(jogador.get('gols_totais'))/qty_partidas,1)} gol por jogo!)")
            break
        
        else:
            print("A quantidade de partidas deve ser maior do que zero!\n\nRepita o processo.")
            continue
    except ValueError:
        print("Ocorreu um erro na hora de sua digitação, revise e tente novamente.")
        continue 
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
    
