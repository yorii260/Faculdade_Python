"""
02) Crie um programa que leia do teclado o nome do trabalhador, ano do seu nascimento e o
número da sua carteira de trabalho (CTPS), juntamente com a idade dele. A idade, deve ser
calculada de acordo com o ano atual e deve ser salva no dicionário também. Se o número da
CTPS for diferente de 0 o programa deve solicitar o ano da contratação do trabalhador. O
sistema deve calcular a idade que o trabalhador irá se aposentar e quantos anos faltam para isso
e salvar no dicionário. Iremos assumir que o tempo de contribuição no INSS são 35 anos de
trabalho (neste exercício não haverá análise pelo sexo, apenas pelo tempo de contribuição.
O programa deve exibir os dados salvos no dicionário. Salientando que, se a CTPS for igual 0 o
cálculo da aposentadoria não será realizado.
"""

from datetime import datetime 


trabalhadores = []
trabalhador = {}

while True:
    
    try:
        
        nome_do_trabalhador = input("[abc] : Digite o nome do trabalhador: ").strip().title()
        ano_de_nascimento = int(input("[123] : Digite o ano do nascimento: "))
        ctps = int(input("[123] : Digite o número da sua CTPS: ")) 
        tempo_de_contribuicao = 35 
        
        if ctps == 0:
            trabalhador.update({"nome": nome_do_trabalhador, "idade": datetime.now().year - ano_de_nascimento, "ctps": 0})
            trabalhadores.append(trabalhador.copy())
            break 
        
        ano_de_contratacao = int(input("[123] : Digite o ano de sua primeira contratação: "))
        salario = float(input("[123] : Digite o seu salário R$ "))
        aposentadoria = (tempo_de_contribuicao - (datetime.now().year - ano_de_contratacao)) + (datetime.now().year - ano_de_nascimento)
        
        trabalhador.update({
            "nome": nome_do_trabalhador, 
            "idade": datetime.now().year - ano_de_nascimento,
            "ctps": ctps,
            "ano_de_contrato": ano_de_contratacao,
            "salario": salario,
            "aposentadoria": aposentadoria,
            "qty_anos_aposentadoria": tempo_de_contribuicao - (datetime.now().year - ano_de_contratacao)
        })
        
        trabalhadores.append(trabalhador.copy())
        break 
    except ValueError:
        print("Erro na digitação, tente novamente.")
        continue 


for x in trabalhadores:
        print(
"""
================= Informações do Trabalhador =====================

-> Nome: {}
-> Idade: {}
-> CTPS: {}
{}
""".format(x.get('nome'), x.get('idade'), x.get('ctps'), '-> Ano da primeira contratação: {}\n-> Salário R$ {}\n-> Idade da aposentadoria: {} anos.\n\nFaltam {} anos para você se aposentar.'.format(x.get("ano_de_contrato"), x.get("salario"), x.get("aposentadoria"), x.get("qty_anos_aposentadoria")) if (x.get('ctps') != 0) else '').strip()
)
    