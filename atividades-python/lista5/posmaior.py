lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
maior = 0
pos = 0

while i < len(lista):
    lista[i] = int(input("Digite um numero: "))
    if maior < lista[i]:
        maior = lista[i]
        pos = i+1
    i += 1
print(f"a lista de numeros é {lista}, o numero maior é {maior}, e a posição é {pos}")