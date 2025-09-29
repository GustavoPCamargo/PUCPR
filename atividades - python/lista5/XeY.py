lista = [0, 0, 0, 0, 0, 0, 0, 0]
x = 0
y = 0
i = 0

while i < len(lista):
    lista[i] = int(input("digite um numero: "))
    i += 1
x = int(input("digite o um numero de 0 - 7: "))
y = int(input("digite outro numero de 0 - 7: "))

soma = lista[x] + lista[y]

print(lista)
print(soma)