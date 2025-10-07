palavra = input("Digite uma palavra: ")
vogais = "aeiou"
vogalnum = 0
vogaisT = []

for i in palavra:
    if i in vogais:
        vogaisT.append(i)
        vogalnum += 1
        
print(f"tem {vogalnum} vogais, que são {vogaisT}")