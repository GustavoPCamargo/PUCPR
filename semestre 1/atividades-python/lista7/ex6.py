lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
lista3 = []
lista4 = []


for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista2.append(lista[i])
    else:
        lista3.append(lista[i])
lista4.extend(lista2)
lista4.extend(lista3)

print(lista2, lista3, lista4)