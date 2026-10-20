# Cores de Texto Padrão
def vermelho(texto):
    return f"\033[31m{texto}\033[m"

def verde(texto):
    return f"\033[32m{texto}\033[m"

def amarelo(texto):
    return f"\033[33m{texto}\033[m"

def azul(texto):
    return f"\033[34m{texto}\033[m"

def roxo(texto):
    return f"\033[35m{texto}\033[m"

def ciano(texto):
    return f"\033[36m{texto}\033[m"

def cinza(texto):
    return f"\033[37m{texto}\033[m"

# Variações em Negrito (Estilo Bold)
def vermelho_bold(texto):
    return f"\033[1;31m{texto}\033[m"

def verde_bold(texto):
    return f"\033[1;32m{texto}\033[m"

def amarelo_bold(texto):
    return f"\033[1;33m{texto}\033[m"
