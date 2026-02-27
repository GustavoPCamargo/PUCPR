palavra = input("Digite uma palavra: ")

def inverter (escrita):
    lista = []
    lista.extend(escrita)
    print(list(reversed(lista)))
print(inverter(palavra))
