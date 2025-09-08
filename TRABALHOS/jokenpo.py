import random

começo = int(input("Olá gostaria de começar o jogo de jokenpô em qual modo?\n1. Jogador x Jogador\n2. Jogador x Computador\n3. Computador x Computador\nDigte o numero da opção: "))

while começo > 3 or começo < 1:
    print("\nopção invalida!")
    começo = int(input("1. Jogador x Jogador\n2. Jogador x Computador\n3. Computador x Computador\nDigte uma opção válida: "))

pontosjgdr1 = 0
pontosjgdr2 = 0

recomeçar = 1

if começo == 1:
    print("\nLegal, PVP maroto\n")
    while recomeçar == 1:
        jgdr1 = int(input("Jogador 1, oque desja jogar?\n1. Pedra\n2. Papel\n3. Tesoura\nDigte o numero da opção: "))
        jgdr2 = int(input("Jogador 2, oque desja jogar?\n1. Pedra\n2. Papel\n3. Tesoura\nDigte o numero da opção: "))

        if (jgdr1 == 1 and jgdr2 == 1) or (jgdr1 == 2 and jgdr2 == 2) or (jgdr1 == 3 and jgdr2 == 3):
            print("\nEmpate!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o jogador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (jgdr1 == 1 and jgdr2 == 2) or (jgdr1 == 2 and jgdr2 == 3) or (jgdr1 == 3 and jgdr2 == 1):
            pontosjgdr2 += 1
            print("\nJogador 2 ganhou!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o jogador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (jgdr2 == 1 and jgdr1 == 2) or (jgdr2 == 2 and jgdr1 == 3) or (jgdr2 == 3 and jgdr1 == 1):
            pontosjgdr1 += 1
            print("\nJogador 1 ganhou!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o jogador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if jgdr1 >= 4 or jgdr1 <= 0 or jgdr2 >= 4 or jgdr2 <= 0:
            print("\nJogada invalida!\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

    if recomeçar == 2:
        print(f"\nOk estou finalizando o programa!\nO placar final foi {pontosjgdr1} a {pontosjgdr2}\nObrigado por jogar o jokenpo do Gustavão gameplays")
if começo == 2:
    print("\nLegal, PVE dos cria\n")
    while recomeçar == 1:
        jgdr1 = int(input("Jogador 1, oque desja jogar?\n1. Pedra\n2. Papel\n3. Tesoura\nDigte o numero da opção: "))
        comp1 = random.randint(1, 3)
        print(f"\nO computador escolheu {comp1}")

        if (jgdr1 == 1 and comp1 == 1) or (jgdr1 == 2 and comp1 == 2) or (jgdr1 == 3 and comp1 == 3):
            print("\nEmpate!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o computador esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (jgdr1 == 1 and comp1 == 2) or (jgdr1 == 2 and comp1 == 3) or (jgdr1 == 3 and comp1 == 1):
            pontosjgdr2 += 1
            print("\nComputador ganhou!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o computador esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (comp1 == 1 and jgdr1 == 2) or (comp1 == 2 and jgdr1 == 3) or (comp1 == 3 and jgdr1 == 1):
            pontosjgdr1 += 1
            print("\nJogador 1 ganhou!\n")
            print(f"Jogador 1 esta com {pontosjgdr1} ponto(s), e o computador esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if jgdr1 >= 4 or jgdr1 <= 0 :
            print("\nJogada invalida!\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

    if recomeçar == 2:
        print(f"\nOk estou finalizando o programa!\nO placar final foi {pontosjgdr1} a {pontosjgdr2}\nObrigado por jogar o jokenpo do Gustavão gameplays")
if começo == 3:
    print("\nQuer só assistir? damn")
    while recomeçar == 1:
        comp1 = random.randint(1, 3)
        comp2 = random.randint(1, 3)
        print(f"\nO computador 1 escolheu {comp1} e o computador 2 escolheu {comp2}")

        if (comp1 == 1 and comp2 == 1) or (comp1 == 2 and comp2 == 2) or (comp1 == 3 and comp2 == 3):
            print("\nEmpate!\n")
            print(f"Computador 1 esta com {pontosjgdr1} ponto(s), e o computador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (comp1 == 1 and comp2 == 2) or (comp1 == 2 and comp2 == 3) or (comp1 == 3 and comp2 == 1):
            pontosjgdr2 += 1
            print("\nComputador 2 ganhou!\n")
            print(f"Computador 1 esta com {pontosjgdr1} ponto(s), e o computador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <=0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

        if (comp2 == 1 and comp1 == 2) or (comp2 == 2 and comp1 == 3) or (comp2 == 3 and comp1 == 1):
            pontosjgdr1 += 1
            print("\nComputador 1 ganhou!\n")
            print(f"Computador 1 esta com {pontosjgdr1} ponto(s), e o computador 2 esta com {pontosjgdr2} ponto(s)\n")
            recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))
            if recomeçar >= 3 or recomeçar <=0:
                while recomeçar >= 3 or recomeçar <= 0:
                    print("opção invalida, tente novamente")
                    recomeçar = int(input("Quer jogar novamente?\n1. Sim\n2. não\nDigte o numero da opção: "))

    if recomeçar == 2:
        print(f"\nOk estou finalizando o programa!\nO placar final foi {pontosjgdr1} a {pontosjgdr2}\nObrigado por jogar o jokenpo do Gustavão gameplays")