palavra = input("Digite uma palavra: ")
caracter = input("Digite uma letra: ")

def contar_caracteres (pal, car):
    lista = []
    lista.extend(pal)
    valor = lista.count(car)
    print(f"a palavra {palavra} tem {valor} caracteres {caracter}")

contar_caracteres(palavra, caracter)