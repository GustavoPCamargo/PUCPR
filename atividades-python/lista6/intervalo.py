lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dentro = 0
fora = 0

for i in range(len(lista)):
    lista[i] = int(input("Digite um numero: "))
    if lista[i] >= 10 and lista[i] <= 20:
        dentro += 1
    else:
        fora += 1
print(f"Tem {dentro} entre 10 e 20 e {fora} fora")