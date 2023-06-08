import csv 
import datetime                   #importando bibliotecas

class Pesquisa():
    def __init__(self):
        self.__idade = ""
        self.__genero = ""        #criando classe pesquisa
        self.respostas = []
    #-----------------------------------------------------------------------#
    def obter_idade(self):
        self.__idade = (input("\nSe desejar sair do programa, digite: 00\n\nDigite sua idade: "))

    def get_idade(self):
        return self.__idade     # obtendo dados usuarios/idade e genero

    def obter_genero(self):
        self.__genero = input("\nVocê se identifica com qual gênero?: ")

    def get_genero(self):
        return self.__genero
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------#
    def questionario(self):
        respostas_usuario = {}                        # criando dicionario
        respostas_usuario["idade"] = self.get_idade()
        respostas_usuario["genero"] = self.get_genero()

        respostas_usuario["pergunta1"] = input("\nUtiliza o Ifood com frequência?: ")     #add as respostas ao dicionarios
        respostas_usuario["pergunta2"] = input("\nO formato de serviço de entrega te agrada?: ")
        respostas_usuario["pergunta3"] = input("\nO aplicativo Ifood melhorou sua vida?: ")
        respostas_usuario["pergunta4"] = input("\nRecomendaria o Ifood para outras pessoas?: ")
        respostas_usuario["data_hora"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.respostas.append(respostas_usuario)     # add as respostas na lista resposta
    #----------------------------------------------------------------------------------------------------------------------------------------#
    def mostra_respostas(self):
        resposta_usuario = self.respostas[-1]  # mostra resposta na tela
        print(f"\n*Respostas adicionadas na base de dados* \n\nInformações do entrevistado:\nIdade = {self.get_idade()} \nGênero = {self.get_genero()}\n")
        print(f"Respostas das perguntas:\nPergunta 1 = {resposta_usuario['pergunta1']} \nPergunta 2 = {resposta_usuario['pergunta2']} \nPergunta 3 = {resposta_usuario['pergunta3']} \nPergunta 4 = {resposta_usuario['pergunta4']}")

    def criar_csv(self):             # criando arquivo csv
        with open("Pesquisa_Ifood.csv", "w", newline="", encoding="utf-8") as pesquisa_csv:
            cabecalho = list(self.respostas[0].keys())
            writer = csv.DictWriter(pesquisa_csv, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(self.respostas)
#----------------------------------------------------------------------------------------------------------------------------------------------#
pesquisa_ifood = Pesquisa()      # criando objeto

while True:         # criando laço de repetiçao
    print("\n Bem vindo a pesquisa do Ifood!")
    pesquisa_ifood.obter_idade()
    if pesquisa_ifood.get_idade() == "00":  # encerra o codigo
        print("\nPesquisa Finalizada")
        exit()
    pesquisa_ifood.obter_genero()
    pesquisa_ifood.questionario()
    pesquisa_ifood.mostra_respostas()
    pesquisa_ifood.criar_csv()
    print()
    print("Obrigado por responder nossa pesquisa!") #mensagem de agradecimento
    print("#"*50)



# Melhorias

# adicionar recurso de respostas em 3 números:
# 1 para sim, 2 para não, 3 para não sei responder
# transformar o número em palavras através de uma função