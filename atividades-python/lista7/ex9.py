import random

lista = list("abcdefghijklmnopqrstuvwxyz")

print(f"Vou randomizar o alfabeto, tente achar a posição da letra a")

random.shuffle(lista)

posição = lista.index("a")

escolha = int(input("Digite uma posição de 1 - 26: ")) - 1



if escolha == posição:
    print(f"Parabens vc acertou! \n")
else:
    print(f"Que pena vc errou! \n")
print(lista)