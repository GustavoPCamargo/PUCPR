a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

def maiornum (a, b, c):
    if a > (b and c):
        return a
    if b > (a and c):
        return b
    if c > (b and a):
        return c
    else:
        max(a, b, c)

print(maiornum (a, b, c))