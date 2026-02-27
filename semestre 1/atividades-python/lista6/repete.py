v = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

cont = 0
mais_repetido = 0
maior_contagem = 0

for i in range(len(v)):
    for j in range(len(v)):
        if v[i] == v[j]:
            cont += 1
            if cont > maior_contagem:
                maior_contagem = cont
                mais_repetido = v[i]
    cont = 0
print(f"o numero mais repetido é {mais_repetido}, que aparece {maior_contagem}")
