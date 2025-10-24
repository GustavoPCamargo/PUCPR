matriz = []

for i in range(5):
    linha = []
    for j in range(1):
        numM = int(input("Digite os numeros da matricula: "))
        linha.append(numM)
        numP = float(input("Digite a media das notas das provas: "))
        linha.append(numP)
        numT = float(input("Digite a media das notas dos trabalhos: "))
        linha.append(numT)
        numF = numP + numT
        linha.append(numF)
    matriz.append(linha)

maior = 0
matricula = 0


for i in range(5):
    for j in range(1):
        if matriz[i][3] > maior:
            maior = matriz[i][3]
            matricula = matriz[i][0]


for i in matriz:
    print(i)

print(f"A matricula do aluno que obteve a maior media é {matricula} que teve {maior} de media")
