lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
par = 0
impar = 0

for i in range(len(lista)):
    lista[i] = int(input("Digite um numero: "))
    if lista[i] % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Tem {par} par e {impar} impar")