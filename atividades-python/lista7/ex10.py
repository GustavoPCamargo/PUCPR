print("Vamos jogar o jogo da velha, digite a posição em q deseja jogar")

a = ["", "", ""]
b = ["", "", ""]
c = ["", "", ""]

print(f"a{a}\nb{b}\nc{c}")

vencedor = 0

while vencedor == 0:
    linha = input("Em qual linha quer jogar? ")
    coluna = int(input("Em qual posição quer jogar? de 1 a 3: ")) - 1

    posição = linha.index(f"{coluna}")

    posição = "X"

    print(f"a{a}\nb{b}\nc{c}")



# NÃO CONSEGUI FAZER :(
