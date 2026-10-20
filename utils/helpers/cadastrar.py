from utils.colors.cores import verde_bold
from utils.colors.cores import roxo
from utils.colors.cores import vermelho_bold

def cadastro_usuarios():

    print(roxo("="*35))
    print(roxo("    Realizar Cadastro"))
    print(roxo("="*35))

    try:
        cfp_digitado = int(input("Digite seu CPF"))


    except ValueError:
        print(vermelho_bold("\nERRO,Digite um valor valido"))

    

    


