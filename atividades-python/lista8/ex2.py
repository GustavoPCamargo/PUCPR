matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        num = int(input(f"Digite um numero: "))
        linha.append(num)
    matriz.append(linha)

print("matrix: ")
for i in matriz:
    print(i)

maior = num
linhaMaior = 0
colunaMaior = 0


for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linhaMaior = i
            colunaMaior = j

print(f"o maior valor é {maior}, que esta localizado na linha {linhaMaior + 1}, e na coluna {colunaMaior + 1}")