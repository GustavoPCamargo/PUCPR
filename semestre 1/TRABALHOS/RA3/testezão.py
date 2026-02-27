matriz = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 2
        else:
            matriz[i][j] = 1
for i in matriz:
    print(i)