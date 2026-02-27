import random
#from colorama import Fore, Style, init
#init(autoreset=True)

matriz = [
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10
    ]
matrizComp = [
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10
    ]
matrizview = [
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10
]

def ataqueComp ():
    contComp = 0
    linha = random.randint(1, 5) - 1
    coluna = random.randint(1, 10) - 1
    if matriz[linha][coluna] == "X":
        print("O computador acertou!")
        matriz[linha][coluna] = "X"
        contComp += 1
        for m in matriz:
            print(m)
    else:
        print("O computador errou!")
        matriz[linha][coluna] = "O"
        for m in matriz:
            print(m)
        
def ataquePlayer():
    contPlayer = 0
    print("\nVamos escolher as posições que deseja atacar.")
    for m in matrizview:
        print(m)
    linha = int(input("Qual linha vai atacar? ")) - 1
    coluna = int(input("Qual coluna vai atacar? ")) - 1
    while matrizview[linha][coluna] == "X" or matrizview[linha][coluna] == "O":
        print("Você ja tentou atacar esta linha e coluna, tente novamente.")
        linha = int(input("Qual linha vai atacar? ")) - 1
        coluna = int(input("Qual coluna vai atacar? ")) - 1
    if matrizComp[linha][coluna] == "X":
        print("Acertou!")
        contPlayer += 1
        matrizview[linha][coluna] = "X"
        for m in matrizview:
            print(m)
    else:
        print("Errou!")
        matrizview[linha][coluna] = "O"
        for m in matrizview:
            print(m)
    

def posComp ():
    for i in range(5):
        linha = random.randint(1, 5) - 1
        coluna = random.randint(1, 10) - 1
        matrizComp[linha][coluna] = "X"

def posPlayer ():
    print("\nPrimeiro vamos decidir as posições de cada embarcação sua")
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
    print("\nPosições decididas, agora vamos começar o jogo")

def jogo ():
    começo = 1
    terminar = False
    contComp = 0
    contPlayer = 0
    while começo == 1: 
        print("Bem vindo ao jogo de batalha naval do Gustavo cray cray")
        posPlayer()
        posComp()
        while terminar == False:
            ataquePlayer()
            ataqueComp()
            if contPlayer >= 5:
                terminar == True
                print("Parabéns vc ganhou o jogo :)")
            if contComp >= 5:
                terminar == True
                print("Que pena o computador ganhou :(")
        começo = int(input("Quer jogar novamente?\n1. Sim\n2. Não\n Digite i numero da opção: "))

jogo()