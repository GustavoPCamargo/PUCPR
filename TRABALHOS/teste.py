num = int(input("digite um numero: "))
cont = 0
par = 0
impar = 0
maior = num
menor = num
while cont < 9:
    if num % 2 == 0:
        par += 1
    else:
        impar +=1
    if num > maior:
        maior = num
    else:
        maior = maior
    if num < menor:
        menor = num
    else:
        menor = menor
    num = int(input("digite um numero: "))
    cont += 1
print(f"maior é {maior} menor {menor} impar{impar} par{par}")