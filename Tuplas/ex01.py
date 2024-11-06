"""
01) Faça um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de “um” até “dez”. O usuário deverá informar um número entre 1 e 10 e o programa
deverá exibir o número por extenso. Deve-se fazer a validação dos dados e verificar se o usuário
deseja continuar (use try/exception)
"""

from os import system 
from colorama import Fore 


numeros_extenso = (
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "inco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez"
)


while True:
    
    try:
        numero = int(input("Digite um número qualquer entre 1-10: "))
        
        if numero < 1 or numero > 10:
            raise ValueError
        
        else:
            system('clear' if system == "nt" else 'cls')
            print(f"{Fore.RED}O número{Fore.GREEN} {numero}{Fore.RED} escrito por extenso é: {Fore.MAGENTA}{numeros_extenso[numero-1]}{Fore.RESET}")
        
        
        check = input("Você deseja continuar ? [S/N]: ").lower().strip() 
        
        match check:
            
            case 's':
                continue 
            case 'n':
                print("Ok, o script será encerrado.")
                break; 
            case _:
                break; 
        
        break;
        
    except ValueError:
        print(f"O valor informado de entrada é inválido, tente novamente.")
        continue 