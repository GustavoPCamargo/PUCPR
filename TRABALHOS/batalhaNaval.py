import random
from colorama import Fore, Style, init
init(autoreset=True)

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
matrizViewComp = [
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10,
    ["#"]*10
]

def colorir(matriz):
    for linha in matriz:
        linha_colorida = []
        for elemento in linha:
            if elemento == "X":
                linha_colorida.append(Fore.GREEN + elemento + Style.RESET_ALL)
            elif elemento == "O":
                linha_colorida.append(Fore.RED + elemento + Style.RESET_ALL)
            elif elemento == "#":
                linha_colorida.append(Fore.BLUE + elemento + Style.RESET_ALL)
            else:
                linha_colorida.append(elemento)
        print(" ".join(linha_colorida))

def posComp ():
    for i in range(5):
        linha = random.randint(1, 5) - 1
        coluna = random.randint(1, 10) - 1
        matrizComp[linha][coluna] = "X"
    while matriz[linha][coluna] == "X":
        linha = random.randint(1, 5) - 1
        coluna = random.randint(1, 10) - 1
        matrizComp[linha][coluna] = "X"
    

def posPlayer ():
    print("\nPrimeiro vamos decidir as posições de cada embarcação sua")
    print("Tabuleiro do Jogador")
    colorir(matriz)
    for i in range(5):
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
            while linha > 4 or linha < 0:
                print("Esta linha não esta no escopo do tabuleiro, tente novamente")
                linha = int(input("Digite a linha em qual deseja colocar a sua embarcação: ")) - 1
            coluna = int(input("Digite a coluna em qual deseja colocar a sua embarcação: ")) - 1
            while coluna > 9 or coluna < 0:
                print("Esta coluna não esta no escopo do tabuleiro, tente novamente")
                coluna = int(input("Digite a coluna em qual deseja colocar a sua embarcação: ")) - 1
        matriz[linha][coluna] = "X"
        print("Tabuleiro do Jogador")
        colorir(matriz)
        print(f"{4 - i} embarcações restantes")
    print("\nPosições decididas, agora vamos começar o jogo")

def ataqueComp ():
    linha = random.randint(1, 5) - 1
    coluna = random.randint(1, 10) - 1
    while matrizViewComp[linha][coluna] == "X" or matrizViewComp[linha][coluna] == "O":
        linha = random.randint(1, 5) - 1
        coluna = random.randint(1, 10) - 1        
    if matriz[linha][coluna] == "X":
        print("O computador acertou!")
        matrizViewComp[linha][coluna] = "X"
        print("Tabuleiro do Jogador")
        colorir(matrizViewComp)
    else:
        print("O computador errou!")
        matrizViewComp[linha][coluna] = "O"
        print("Tabuleiro do Jogador")
        colorir(matrizViewComp)
        
def ataquePlayer():
    linha = int(input("Qual linha vai atacar? ")) - 1
    while linha > 4 or linha < 0:
        print("Esta linha não esta no escopo do tabuleiro, tente novamente")
        linha = int(input("Qual linha vai atacar? ")) - 1
    coluna = int(input("Qual coluna vai atacar? ")) - 1
    while coluna > 9 or coluna < 0:
        print("Esta coluna não esta no escopo do tabuleiro, tente novamente")
        coluna = int(input("Qual coluna vai atacar? ")) - 1
    while matrizview[linha][coluna] == "X" or matrizview[linha][coluna] == "O":
        print("Você ja tentou atacar esta linha e coluna, tente novamente.")
        linha = int(input("Qual linha vai atacar? ")) - 1
        while linha > 4 or linha < 0:
            print("Esta linha não esta no escopo do tabuleiro, tente novamente")
            linha = int(input("Qual linha vai atacar? ")) - 1
        coluna = int(input("Qual coluna vai atacar? ")) - 1
        while coluna > 9 or coluna < 0:
            print("Esta coluna não esta no escopo do tabuleiro, tente novamente")
            coluna = int(input("Qual coluna vai atacar? ")) - 1
    if matrizComp[linha][coluna] == "X":
        print("Acertou!")
        matrizview[linha][coluna] = "X"
        print("Tabuleiro do Computador")
        colorir(matrizview)
    else:
        print("\nErrou!")
        matrizview[linha][coluna] = "O"
        print("Tabuleiro do Computador")
        colorir(matrizview)

def jogo ():
    começo = 1
    terminarJogo = False
    while começo == 1: 
        print("Bem vindo ao jogo de batalha naval do Gustavo cray cray")
        posPlayer()
        posComp()
        print("\nVamos escolher as posições que deseja atacar.")
        print("Tabuleiro do Computador")
        colorir(matrizview)
        while terminarJogo == False:
            ataquePlayer()
            contPlayer = 5 - (matrizview[0].count("X") + matrizview[1].count("X") + matrizview[2].count("X") + matrizview[3].count("X") + matrizview[4].count("X"))
            print(f"\n {contPlayer} Embarcações inimigas restantes\n")
            ataqueComp()
            contComp = 5 - (matrizViewComp[0].count("X") + matrizViewComp[1].count("X") + matrizViewComp[2].count("X") + matrizViewComp[3].count("X") + matrizViewComp[4].count("X"))
            print(f"\n {contComp} Embarcações aliadas restantes")
            if contPlayer == 0:
                print("Parabéns você ganhou do computador :)")
                terminarJogo = True
            if contComp == 0:
                print("Que pena o computador venceu :(")
                terminarJogo == True
        começo = int(input("\nQuer jogar novamente?\n1. Sim\n2. Não\n Digite o número da opção: "))
jogo()