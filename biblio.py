'''
Neste arquivo está as funções de aparência da pesquisa e de verificação de numeros inteiros.
'''

import constants

#Esta função faz com que o usuário digite apenas numeros inteiros.
def digit_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError , TypeError):
            print(f'\033[31m{constants.ERRO_INT}\033[m')
            continue
        else:
            return num

# Incluir linha para separação de tópicos
def linha(tamanho = 80):
    return '=' * tamanho


# Função para edição do cabeçalho da pesquisa
def cabecalho(texto1 , texto2 , texto3):
    print(linha())
    print('\n')
    print(texto1.center(80))
    print()
    print(texto2.center(80))
    print(texto3.center(80))
    print('\n')
    print(linha())

# Função para edição do rodapé da pesquisa
def rodape(texto):
    print('\n')
    print(texto.center(80))
    print('\n')

def encerra(texto):
    print('\n\n')
    print(texto.center(80))
    print('\n\n')