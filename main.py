from utils.helpers.exit import SAIR
from utils.colors.cores import roxo
from utils.colors.cores import amarelo_bold
from utils.colors.cores import vermelho_bold

print(roxo("="*35))
print(roxo("  Bem vindo(a) ao   DGcash"))
print(roxo("="*35))

while True:

    print(amarelo_bold("="*35))
    print(amarelo_bold("   1-SAIR"))
    print(amarelo_bold("   2-CADASTRAR-SE"))
    print(amarelo_bold("="*35))

    try:
        escolha = int(input(amarelo_bold("Escolha: ")))

    except ValueError:
        print(vermelho_bold("\nERRO,Digite um valor valido"))



    match escolha:
      
        case 1:
            SAIR()
            break

        case 2:
            print()


        case _:
            print(vermelho_bold("\nERRO,Digite um valor valido"))

        
        


