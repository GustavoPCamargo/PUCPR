num = int(input("digite um numero: "))

par = 0
impar = 0

cont = 1

while cont <=10:
    num = int(input("digite um numero: "))
    cont += 1
    if num % 2 == 0:
        par += 1
    else:
        impar += 1


print(f"deu {par} par e {impar} impar")