import random

numerosjogador1 = []
numerosjogador2 = []

num1 = 0
num2 = 0

soma1 = 0
soma2 = 0

vencedor = ""

for i in range(0, 3):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    soma1 += num1
    soma2 += num2
    numerosjogador1.append(num1)
    numerosjogador2.append(num2)

if soma1 > soma2:
    vencedor = "jogador 1"
elif soma1 == soma2:
    vencedor = "impate"
else:
    vencedor = "jogador 2"



print(f"a rolagem do jogador 1 foi {numerosjogador1} e o jogador 2 foi {numerosjogador2}, o jogador 1 teve {soma1} pontos e jogador 2 teve {soma2} pontos, o vencedor é {vencedor}")

