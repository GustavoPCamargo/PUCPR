palavra = input("Digite uma palavra: ")

def e_polidromo (escrita):
    lista = []
    lista.extend(escrita)
    inverso = list(reversed(lista))
    if inverso == lista:
        return "é polidromo"
    else: 
        return "não é polidromo"

print(e_polidromo(palavra))