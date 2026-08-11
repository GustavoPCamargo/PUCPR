import random

lista = []

tamanho = int(input("Diga o tamanho da lista: "))

def lista_aleatoria (lista, tamanho):
    for i in range(tamanho):
        num = random.randint(1, 100)
        if num % 3 == 0:
            lista.append(f"{num} - numero é multiplo de 3")
        elif num % 2 == 0:
            lista.append(f"{num} - numero é par")
        elif not(num % 2 == 0):
            lista.append(f"{num} - numero é impar")      
        else:
            num = 0

    return lista


print(lista_aleatoria(lista,tamanho))