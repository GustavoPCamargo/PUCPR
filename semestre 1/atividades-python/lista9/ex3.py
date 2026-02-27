lista = []

for i in range(5):
    num = int(input("Digite um numero: "))
    lista.append(num)

print(lista)

def maior_elemento(elementos):
    maior = max(elementos)
    return maior

print(maior_elemento(lista))