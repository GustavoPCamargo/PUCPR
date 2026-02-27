numeros = [5, 7, 12, 2, 9, 21]

numeros[1] = 17
numeros[3] = 22
numeros[2] = 1
numeros[4] = 29

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])

soma = numeros[5] + numeros[4]
sub = numeros[3] - numeros[1]
mult = numeros[0] * numeros[5]
div = numeros[3] / numeros[2]

print(soma)
print(sub)
print(mult)
print(div)

i = 0

while i < 6:
    if numeros[i] % 2 == 0:
        print(numeros[i])
        i += 1
    else:
        i+=1