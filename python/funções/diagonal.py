matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input("Digite um valor: "))
        linha.append(num)
    matriz.append(linha)

for i in matriz:
    print(i)

def imprime_diagonal (a):
    for i in range(len(a)):
        print(a[i][i])

imprime_diagonal(matriz)

