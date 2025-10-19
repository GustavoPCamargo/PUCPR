lista = []

pala = ""
maior = ""
menor = "ooooooooooooooooooooooooooooooooooooooo"


for i in range(5):
    pala = (input("Digite uma palavra: "))
    lista.append(pala)
for i in range(len(lista)):
    if len(lista[i]) > len(maior):
        maior = lista[i]
    if len(lista[i]) < len(menor):
        menor = lista[i]

print(f"A lista é {lista}, a maior palavra é {maior}, e a menor é {menor}")