lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
maior = lista[i]
menor = 99999

while i < len(lista):
    lista[i] = int(input("Digite um numero: "))
    if maior < lista[i]:
        maior = lista[i]
    if menor > lista[i]:
        menor = lista[i]
    i += 1
print(lista)
print(f"o maior é {maior} e o menor é o {menor}")