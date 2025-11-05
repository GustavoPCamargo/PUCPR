import random

matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


def menu ():
    print("Bem vindo ao jogo de batalha naval do Gustavo cray cray")
    print("Primeiro vamos decidir as posições de cada embarcação sua")
    for i in range(5):
        for m in matriz:
            print(m)
        linha = int(input("Digite a linha em qual deseja colocar a sua embarcação: ")) - 1
        while linha > 4 or linha < 0:
            print("Esta linha não esta no escopo do tabuleiro, tente novamente")
            linha = int(input("Digite a linha em qual deseja colocar a sua embarcação: ")) - 1
        coluna = int(input("Digite a coluna em qual deseja colocar a sua embarcação: ")) - 1
        while coluna > 9 or coluna < 0:
            print("Esta coluna não esta no escopo do tabuleiro, tente novamente")
            coluna = int(input("Digite a coluna em qual deseja colocar a sua embarcação: ")) - 1
        while matriz[linha][coluna] == "X":
            print("Esta linha e coluna ja estão sendo utilizadas, tente novamente")
            linha = int(input("Digite a linha em qual deseja colocar a sua embarcação: ")) - 1
            coluna = int(input("Digite a coluna em qual deseja colocar a sua embarcação: ")) - 1
        matriz[linha][coluna] = "X"
        for m in matriz:
            print(m)
        print(f"{4 - i} embarcações restantes")
    print("posições decididas, agora vamos começar o jogo")
def jogo ():
    print("O computador já decidiu as posições")
menu()














