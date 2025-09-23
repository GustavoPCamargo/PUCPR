import random

mega = [random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)]
pos = 1

aposta = int(input(f"Digite o {pos}º numero para apostar na mega de 1 a 60: "))
Napostas = [aposta, 0, 0, 0, 0, 0]

acertos = 0

i = 0
while i < 5:
    if aposta == mega[i]:
        acertos += 1
        print("acertou!")
        i +=1
        pos +=1
        aposta = int(input(f"Digite o {pos}º numero para apostar na mega de 1 a 60: "))
        Napostas[i] += aposta
    else:
        print("errou")
        i+= 1
        pos +=1
        aposta = int(input(f"Digite o {pos}º numero para apostar na mega de 1 a 60: "))
        Napostas[i] += aposta
        
print(f"os numeros eram {mega} vc apostou {Napostas} vc acertou {acertos}")