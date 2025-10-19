
#1, -------------------- #
import random


lista1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista2 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range(10):
    lista1[i] = int(input("Digite um numero: "))
    lista2[i] = lista1[i]
for i in range(len(lista1)):
    for j in range(i+1, 10):
        if lista1[i] == lista2[i]:
            lista2[i] = random.randint 
print(lista1)
print(lista2)
#2, -------------------- #
lista = [10,20,30,40,50,60]
listaf = []
a = 5
for i in range(0,3):
    listaf.append(lista[i])
    listaf.append(lista[a])
    a -=1


print(listaf)
#3, -------------------- #
pesopessoas = []

while True:
    pesotemp = int(input("digite o peso da pessoa que entrou: "))
    pesopessoas.append(pesotemp)
    limite = sum(pesopessoas)
    print(f"o peso atual é {limite} KG")
    if limite >= 200:
        break
print(f"entram {len(pesopessoas)} pessoas antes de bater o limite")