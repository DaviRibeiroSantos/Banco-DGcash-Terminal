import re
from utils.colors.cores import vermelho_bold

def validador_cfp(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        
        print(vermelho_bold("="*35))
        print(vermelho_bold("\n  ERRO,Digite um  cpf valido"))
        print(vermelho_bold("="*35))
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
            
    return True

    entrada = input("Digite o CPF: ")

    if validar_cpf(entrada):
        print("Válido!")
    
    else:
        print("Inválido!")
