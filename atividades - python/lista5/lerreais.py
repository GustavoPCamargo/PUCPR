real = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
quadrado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(real):
    real[i] = float(input("Digite um numero: "))
    quadrado[i] = real[i] ** 2
    i += 1
print(real)
print(quadrado)