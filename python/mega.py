import random

mega = [random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)]

aposta = int(input("Digite 6 numeros para apostar na mega de 1 a 60"))

acertos = 0

if aposta == mega[1]:
    acertos += 1


