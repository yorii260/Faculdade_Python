"""
03) Faça um programa que crie uma matriz de ordem 3, e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela com a formatação correta (mxn)

Exemplo de matriz: 

[a11 a12 a13]
[a21 a22 a23]
[a31 a32 a33]

04) Aprimore o exercício anterior e mostre no final:
a) a soma de todos os valores digitados
b) A soma dos valores pares
c) A soma dos valores da terceira coluna
d) O maior valor da segunda linha

"""

# 3: ----------------------------------------- // -------------------------------------------

from os import system 


matriz = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]


i = 1 
j = 1

matriz_pos = 0 

while True:

    try:
        if j > 3:
            i += 1 
            j = 1 
        
        system('clear' if system == "nt" else 'cls')
        
        number = int(input(f"[{i}:{j}] : Informe o valor da posição a{i}{j}: "))
        matriz[matriz_pos] = number 
        
        j+= 1
        matriz_pos += 1 
        
        if i == 3 and j == 4:
            break 
        
    except ValueError:
        print("Digite apenas números, tente novamente.")
        continue


print(
f"""
[{matriz[0]} {matriz[1]} {matriz[2]}]
[{matriz[3]} {matriz[4]} {matriz[5]}]
[{matriz[6]} {matriz[7]} {matriz[8]}] 3x3
"""
)
    
# -------------------------------------------------- // ----------------------------------------------------

# 4: 
pares = [0, []]

for i in matriz:
    
    if i % 2 == 0:
        pares[0] += i 
        pares[1].append(str(i))


print(
f"""
=====================================================================
B) A soma de todos os valores pares é {pares[0]} | {','.join(pares[1])}.
C) A soma dos valores da terceira coluna é {matriz[2] + matriz[5] + matriz[8]}.
D) O maior valor da segunda linha é {max(matriz[3:6])} | {','.join([str(f) for f in matriz[3:6]])}
=====================================================================
"""
)