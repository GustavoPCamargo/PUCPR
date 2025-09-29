recomeçar = 1

while recomeçar == 1:
    a = float(input("digite o primeiro valor: "))
    b = float(input("digite o segundo valor: "))

    operação = int(input("qual a operação que deseja fazer entre os 2 valores \n1. Soma\n2. Subtração \n3. Multipicação \n4. Divisão \nDigite o numero da opção: "))
    if operação == 1:
        print(f"{a} + {b} = {a + b}")
        recomeçar = int(input("quer fazer outra conta? \n1. Sim\n2. Não\nDigite o numero da opção: "))
    elif operação == 2:
        print(f"{a} - {b} = {a - b}")
        recomeçar = int(input("quer fazer outra conta? \n1. Sim\n2. Não\nDigite o numero da opção: "))
    elif operação == 3:
        print(f"{a} * {b} = {a * b}")
        recomeçar = int(input("quer fazer outra conta? \n1. Sim\n2. Não\nDigite o numero da opção: "))
    elif operação == 4:
        print(f"{a} / {b} = {a / b}")
        recomeçar = int(input("quer fazer outra conta? \n1. Sim\n2. Não\nDigite o numero da opção: "))
    else:
        print("Valor invalido")
if recomeçar == 2:
    print("\nblz estou acabando o programa") 