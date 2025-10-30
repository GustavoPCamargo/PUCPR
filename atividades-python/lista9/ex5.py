def somar (a, b):
    soma = a + b
    return soma
def sub (a, b):
    sub = a - b
    return sub
def mult (a, b):
    mult = a * b
    return mult
def div (a, b):
    div = a / b
    return div

def menu ():
    começo = 1
    while começo == 1:
        print("Ola esta é a calculadora do gusão")
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))
        operação = int(input("Qual operação deseja fazer \n1. soma\n2. subtração \n3. multiplicação\n4. divisão\nDigite o numero da opção: "))
        if operação == 1:
            print(somar(x, y))
        if operação == 2:
            print(sub(x, y))
        if operação == 3:
            print(mult(x, y))
        if operação == 4:
            print(div(x, y))
        começo = int(input("Quer recomeçar?\n1. Sim\n2. não\n Digite o valor da opção"))
menu()