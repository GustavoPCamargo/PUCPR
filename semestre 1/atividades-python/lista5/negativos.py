lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
nega = 0
soma = 0

while i < len(lista):
    lista[i] = float(input("Digite um numero real: "))
    if lista[i] < 0:
        nega += 1
    if lista[i] >= 0:
        soma += lista[i]
    i += 1
print(f"o vetor foi {lista}, negativos {nega}, a soma dos positivos {soma}")