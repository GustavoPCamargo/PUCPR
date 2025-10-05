lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(lista)):
    lista[i] = int(input("Digite um numero: "))

for i in range(len(lista)):
    for j in range(i + 1, 10):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print("A ordem crescente é")
for n in lista:
    print(n)
