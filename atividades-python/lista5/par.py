lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
par = 0
i = 0

while i < len(lista):
    lista[i] = int(input("Digite um numero: "))
    if lista[i] % 2 == 0:
        par += 1
    i += 1
print(lista)
print(f"tem {par} par")
