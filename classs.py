import constants
from biblio import *
import csv 
import datetime


class Pesquisa():
    """
    Classe utilizada para realização de pesquisas.

    Atributos:
        - idade: apenas numeros inteiros
        - genero: cisgenero, transgenero ou não-binario
    
    Métodos:
        - init >  método construtor que armazena a idade e gênero do usuário;
        - obter_idade > solicita a idade do usuário e caso digite 00 finaliza o programa;
        - get_idade > retorna o resultado solicitado no método anterior;
        - verificacao_genero > verifica se a entrada do usuário é uma opção de gênero existente;
        - obter_genero > solicita o gênero do usuário;
        - get_genero > retorna o resultado solicitado no método anterior;
        - verificacao_respostas > verifica se a entrada do usuario é uma opção de resposta existente;
        - questionario > faz a perguntas ao usuário e adiciona em uma lista respostas que está no construtor;
        - mostrar_respostas > mostra um relatório do que o usuário respondeu e que foi armazenado no banco de dados com data e hora;
        - criar_csv > cria um arquivo csv (comma separated values) com o resultado da pesquisa.
    """
    def __init__(self):
        #Inicializando a classe pesquisa
        self.__idade = ""
        self.__genero = ""
        self.respostas = []

    def obter_idade(self):
        #Solicitando idade
        self.__idade = digit_int(f'{constants.PERGUNTA_INICIO_1_1}\n>>> ')

    def get_idade(self):
        #Retornando idade
        return self.__idade
    
    def verificacao_genero(self , msg):
        generos = {1:{constants.GENERO_1} , 2:{constants.GENERO_2} , 3:{constants.GENERO_3} , 4:{constants.GENERO_4}}
        while True:
            try:
                usuario = int(input(msg))
                if usuario in generos:
                    return generos[usuario]
                else:
                    print(f'\033[31m{constants.ERRO_INT}\033[m')
            except (TypeError , ValueError , KeyError):
                print(f'\033[31m{constants.ERRO_STR}\033[m')
                continue

    def obter_genero(self):
        #Solicitando gênero
        self.__genero = self.verificacao_genero(f'\n\n{constants.PERGUNTA_INICIO_1_2}\n{constants.OPCOES_GENEROS}\n>>> ')

    def get_genero(self):
        #Retornando gênero
        return self.__genero

    def verificacao_respostas(self , msg2):
        generos = {1:{constants.RESPOSTA_1} , 2:{constants.RESPOSTA_2} , 3:{constants.RESPOSTA_3}}
        while True:
            try:
                usuario2 = int(input(msg2))
                if usuario2 in generos:
                    return generos[usuario2]
                else:
                    print(f'\033[31m{constants.ERRO_INT}\033[m')
            except (ValueError , TypeError , KeyError):
                print(f'\033[31m{constants.ERRO_STR}\033[m')

    def questionario(self):
        #Perguntando ao usuário e armazenando na lista respostas
        respostas_usuario = {}
        respostas_usuario["idade"] = self.get_idade()
        respostas_usuario["genero"] = self.get_genero()

        respostas_usuario["pergunta1"] = self.verificacao_respostas(f"\n{constants.PERGUNTA_1}\n{constants.OPCOES_RESPOSTAS}\n>>> ")
        respostas_usuario["pergunta2"] = self.verificacao_respostas(f"\n{constants.PERGUNTA_2}\n{constants.OPCOES_RESPOSTAS}\n>>> ")
        respostas_usuario["pergunta3"] = self.verificacao_respostas(f"\n{constants.PERGUNTA_3}\n{constants.OPCOES_RESPOSTAS}\n>>> ")
        respostas_usuario["pergunta4"] = self.verificacao_respostas(f"\n{constants.PERGUNTA_4}\n{constants.OPCOES_RESPOSTAS}\n>>> ")
        respostas_usuario["data_hora"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.respostas.append(respostas_usuario)
    
    def mostra_respostas(self):
        #Exibindo relatório de repostas do usuário
        resposta_usuario = self.respostas[-1]
        rodape('**RESPOSTAS ADICIONADAS NA BASE DE DADOS**')
        print(f"\nInformações do entrevistado:\nIdade = {self.get_idade()} \nGênero = {self.get_genero()}\n")
        print(f"Respostas das perguntas:\nPergunta 1 = {resposta_usuario['pergunta1']} \nPergunta 2 = {resposta_usuario['pergunta2']} \nPergunta 3 = {resposta_usuario['pergunta3']} \nPergunta 4 = {resposta_usuario['pergunta4']}")

    def criar_csv(self):
        #Criando o arquivo CSV e armazenando as respostas
        with open("Pesquisa_Ifood.csv", "w", newline="", encoding="utf-8") as pesquisa_csv:
            cabecalho = list(self.respostas[0].keys())
            writer = csv.DictWriter(pesquisa_csv, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(self.respostas)
