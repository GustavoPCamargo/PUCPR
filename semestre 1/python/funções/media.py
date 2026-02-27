lista = []

for i in range(5):
    valor = int(input("Digite um numero: "))
    lista.append(valor)

def media (a):
    soma = 0
    for i in range(len(a)):
        soma += a[i]
        media = soma / len(a)
    return media

print(media(lista))
