import csv 
import datetime

class Pesquisa():
    def __init__(self):
        self.__idade = ""
        self.__genero = ""
        self.respostas = []
    #-----------------------------------------------------------------------#
    def obter_idade(self):
        self.__idade = (input("\nSe desejar sair do programa, digite: 00\n\nDigite sua idade: "))

    def get_idade(self):
        return self.__idade

    def obter_genero(self):
        self.__genero = input("\nVocê se identifica com qual gênero?: ")

    def get_genero(self):
        return self.__genero
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------#
    def questionario(self):
        respostas_usuario = {}
        respostas_usuario["idade"] = self.get_idade()
        respostas_usuario["genero"] = self.get_genero()

        respostas_usuario["pergunta1"] = input("\nVocê costuma jogar games Multiplayer?: ")
        respostas_usuario["pergunta2"] = input("\nVocê costuma jogar games Singleplayer?: ")
        respostas_usuario["pergunta3"] = input("\nVocê costuma jogar em dispositívos portáteis?: ")
        respostas_usuario["pergunta4"] = input("\nVocê costuma jogar em dispositivos de mesa?: ")
        respostas_usuario["data_hora"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.respostas.append(respostas_usuario)
    #----------------------------------------------------------------------------------------------------------------------------------------#
    def mostra_respostas(self):
        resposta_usuario = self.respostas[-1]
        print(f"\n*Respostas adicionadas na base de dados* \n\nInformações do entrevistado:\nIdade = {self.get_idade()} \nGênero = {self.get_genero()}\n")
        print(f"Respostas das perguntas:\nPergunta 1 = {resposta_usuario['pergunta1']} \nPergunta 2 = {resposta_usuario['pergunta2']} \nPergunta 3 = {resposta_usuario['pergunta3']} \nPergunta 4 = {resposta_usuario['pergunta4']}")

    def criar_csv(self):
        with open("Pesquisa_Games.csv", "w", newline="", encoding="utf-8") as pesquisa_csv:
            cabecalho = list(self.respostas[0].keys())
            writer = csv.DictWriter(pesquisa_csv, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(self.respostas)
#----------------------------------------------------------------------------------------------------------------------------------------------#
video_games = Pesquisa()

while True:
    print("\n Bem vindo a pesquisa de Jogos!")
    video_games.obter_idade()
    if video_games.get_idade() == "00":
        print("\nPesquisa Finalizada")
        exit()
    video_games.obter_genero()
    video_games.questionario()
    video_games.mostra_respostas()
    video_games.criar_csv()
    print()
    print("Obrigado por responder nossa pesquisa!")
    print("#"*50)