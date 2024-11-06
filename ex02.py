"""
02) Crie um tupla preenchida com a classificação atual do campeonato brasileiro, série A
(somente o nome dos clubes) na ordem de colocação. Depois apresente:
a) Os 6 primeiros colocados
b) Os 4 últimos colocados
c) A posição em que está o time Fortaleza
"""

tabela_brasileirao = ( # Tabela retirada da 32a rodada do campeonato.
    "Botafogo",
    "Palmeiras",
    "Fortaleza",
    "Internacional",
    "Flamengo",
    "São Paulo",
    "Bahia",
    "Cruzeiro",
    "Vasco",
    "Atlético-MG",
    "Grêmio",
    "Vitória",
    "Corinthians",
    "FLuminense",
    "Críciuma",
    "Bragantino",
    "Athletico-PR",
    "Juventude",
    "Cuiabá",
    "Atlético-GO"
)

while True:
    
    print(
        f"""
        a) Os seis primeiros colocados são:
        {' '.join(tabela_brasileirao[0:6])}
        
        b) Os quatro ultimos colocados são:
        {' '.join(tabela_brasileirao[16:])}
        
        c) O Fortaleza está atualmente na {tabela_brasileirao.index("Fortaleza")+1}a colocação.
        """
    )
    break