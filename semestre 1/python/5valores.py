lista = [0, 0, 0, 0, 0]


for i in range(len(lista)):
    lista[i] = int(input("Digite um numero inteiro positivo: "))

listaO = sorted(lista)
listaR = sorted(lista, reverse=True)

tamanho = len(lista)

menor = min(lista)
maior = max(lista)

soma = sum(lista)



print(f"A sua lista é {lista}, em ordem crescente é {listaO}, em ordem decrescente {listaR}, o tamanho das listas são {tamanho}, o menor valor é {menor}, o maior valor é {maior}, e a soma de todos os valores é {soma}")