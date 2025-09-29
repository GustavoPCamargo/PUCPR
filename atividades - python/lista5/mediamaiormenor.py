lista = [0, 0, 0, 0, 0]

i = 0
maior = 0
menor = 99999
media = 0

while i < len(lista):
    lista[i] = int(input("Digite um numero: "))
    if maior < lista[i]:
        maior = lista[i]
    if menor > lista[i]:
        menor = lista[i]
    media += lista[i]
    i += 1
media = media / len(lista)

print(f"a lista de numeros foi {lista}, o maior numero é {maior}, o menor numero é {menor} e a media é {media}")