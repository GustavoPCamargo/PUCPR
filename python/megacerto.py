import random

aposta = [0, 0, 0, 0, 0, 0]
mega = [0, 0, 0, 0, 0, 0]

acertos = 0

i = 0
while i < len(aposta):
    aposta[i] = int(input("Digite os 6 numeros que deseja apostar: "))
    i += 1
while i < len(mega):
    ale += random.randint(1, 60)
    j = 0
    repetido = False
    while mega[j] != 0:
        mega += 1
    while i < len(aposta):
        j = 0
    while j < len(mega):
        if aposta[i] == mega[i]:
            acertos += 1
        j += 1
    i += 1

print(f"os numeros certos eram {mega} vc jogou {aposta} e vc acertou {acertos}")