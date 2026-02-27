lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
print(lista)

for i in range(len(lista)):
    lista[i] = lista[i] ** 2
soma = sum(lista)

print(lista)

print("a soma de tudo é", soma)