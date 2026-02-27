a = []
b = []
c = []
soma = 0
n = int(input("Digite o tamanho do vetor: "))

for i in range(n):
    num = int(input("Digite o valor para entrar no vetor A: "))
    a.append(num)
for i in range(n):
    num = int(input("Digite o valor para entrar no vetor B: "))
    b.append(num)
for i in range(n):
    soma = a[i] + b[i]
    c.append(soma)


print(f"A soma dos vetores é {c}")