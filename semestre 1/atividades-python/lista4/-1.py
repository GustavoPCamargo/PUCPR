num = int(input("digite um numero: "))

cont = 0
media = 0

while num != -1:
    cont += 1
    media += num
    num = int(input("digite outro numero: "))

    if num == -1:
        print (f"{media / cont}")