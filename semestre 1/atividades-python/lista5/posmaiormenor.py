lista = [0, 0, 0, 0, 0]

i = 0
maior = 0
menor = 9999999999
maiorpos = 0
menorpos = 0

while i < len(lista):
    lista[i] = int(input("Digite um numero: "))
    if maior < lista[i]:
        maior = lista[i]
        maiorpos = i+1
    if menor > lista[i]:
        menor = lista[i]
        menorpos = i+1
    i += 1
print(f"a lista de numeros foi {lista}, o maior é {maior} na posição {maiorpos}, e o menor é {menor} na posição {menorpos}.")