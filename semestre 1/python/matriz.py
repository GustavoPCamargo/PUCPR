matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
          ]

for i in matriz:
    print(i)


for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(matriz[linha][coluna])

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

print(matriz)

soma = matriz[0][0] + matriz[0][1]
sub = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
div = matriz[1][2] / matriz[0][2]

print(soma, sub, mult, div)