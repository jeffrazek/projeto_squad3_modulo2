from classs import Pesquisa
from biblio import *
import constants

# Criando objeto pesquisa
pesquisa_ifood = Pesquisa()


# Programa
while True:
    cabecalho(f'\033[33m{constants.TITULO_PESQUISA}' , f'{constants.SUB_TIT_1}' , f'{constants.SUB_TIT_2}\033[m')
    pesquisa_ifood.obter_idade()
    pesquisa_ifood.get_idade()
    if pesquisa_ifood.get_idade() == 00:
        encerra(f'\033[33m{constants.FINALIZAÇÃO_DE_PESQUISA}\033[m')
        exit()
    pesquisa_ifood.obter_genero()
    pesquisa_ifood.questionario()
    pesquisa_ifood.mostra_respostas()
    pesquisa_ifood.criar_csv()
    rodape(f'\033[32m{constants.AGRADECIMENTO}\n\033[m')
